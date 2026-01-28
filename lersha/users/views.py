from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from uuid import uuid4
from .models import Farmer
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from users.models import State, City
from market.models import Product, Category
from .forms import FarmerUpdateForm, FarmerUserUpdateForm, ProductUpdateForm, ProductForm
from .decorators import is_farmer, is_subscribed
from users.models import Subscription

@is_farmer
def profile_update(request):
    if request.method == 'POST':
        form = FarmerUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        form_user = FarmerUserUpdateForm(request.POST, instance=request.user)
        if form_user.is_valid():
            if form.is_valid():
                form.save()
                form_user.save()
                messages.success(request, f"Your account has been updated!")
                return redirect('profile-update-page')
            else:
                messages.error(request, f"Your account has not been updated!" + form.errors.as_text())
        else:
            messages.error(request, f"Your account has not been updated!" + form_user.errors.as_text())
            form = FarmerUpdateForm(instance=request.user.profile)
    context = {'cities': City.objects.all(), 'states': State.objects.all()}
    return render(request, 'users/profile-update.html', context=context)

def profile(request, pk):
    farmer = get_object_or_404(Farmer, pk=pk)
    context = {'farmer': farmer}
    if request.user.is_authenticated and request.user.profile == farmer:
        return redirect('profile-update-page')
    return render(request, 'users/profile.html', context=context)

@is_farmer
def farmer_products_list(request):
    if request.user.is_authenticated:
        products = Product.objects.order_by('-id')
        products = products.filter(farmer=request.user.profile)
        categories = Category.objects.all()

        category = request.GET.get('category')
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        search = request.GET.get('search')

        # ✅ APPLY FILTERS FIRST
        if search:
            products = products.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )

        if category:
            products = products.filter(category=category)

        if price_min:
            products = products.filter(price__gte=price_min)

        if price_max:
            products = products.filter(price__lte=price_max)

        # ✅ PAGINATE LAST
        paginator = Paginator(products, 10)
        page_number = request.GET.get('page')
        products_page = paginator.get_page(page_number)

        # ✅ CLEAN QUERYSTRING (FOR FRONTEND LINKS)
        querydict = request.GET.copy()
        querydict.pop('page', None)

        return render(
            request,
            'users/farmer-product-list.html',
            {
                'products': products_page,   # 🔥 MUST be Page object
                'categories': categories,
                'querystring': querydict.urlencode(),
            }
        )

@is_farmer
def farmer_products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Only allow the owning farmer to access this view
    if product.farmer != request.user.profile:
        messages.error(request, "You can only view and edit your own products.")
        return redirect('some-fallback-view')  # e.g., 'farmer-dashboard' or 'home'

    if request.method == "POST":
        # Handle form submission to update the product
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"'{product.name}' has been successfully updated.")
            return redirect('farmer-product-detail', pk=product.pk)
        else:
            messages.error(request, "Please correct the errors in the form. " + form.errors.as_text())
    else:
        # GET request - show the current product and pre-filled form
        form = ProductUpdateForm(instance=product, initial={'category': product.category.name})

    context = {
        'product': product,
        'form': form,
        'categories': Category.objects.all(),
        'is_owner': True,  # Useful in template to show edit controls
    }

    return render(request, 'users/farmer-product-detail.html', context)

@is_farmer
@require_POST  # Only allow POST requests for security
def farmer_product_delete(request, product_id):
    """
    Independent view to delete a product.
    Only the owning farmer can delete their own product.
    """
    product = get_object_or_404(Product, id=product_id)

    # Security: Ensure only the owner can delete
    if product.farmer != request.user.profile:  # Adjust if your farmer field is request.user directly
        messages.error(request, "You are not authorized to delete this product.")
        return redirect('product-detail-page', product_id=product.id)  # or fallback URL

    product_name = product.name  # Save name for success message
    product.delete()

    messages.success(request, f"Product '{product_name}' has been successfully deleted.")

    # Redirect to a safe place after deletion
    return redirect('farmer-product-list')

@is_subscribed
def farmer_product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user.profile
            product.save()
            return redirect('product-list-page')  # Redirect to your product list page
        else:
            messages.error(request, "Please correct the errors in the form." + form.errors.as_text())
    else:
        form = ProductForm()

    return render(request, 'users/farmer-product-create.html', {'form': form, 'categories': Category.objects.all()})


def subcribe(request):
    tx_ref = uuid4()
    farmer = request.user.profile
    if farmer.subscription.first() is not None:
        print(farmer.subscription)
        messages.error(request, "You are already subscribed.")
        return redirect('profile-update-page')
    else:
        print(1)
        return render(request, 'users/subscribe.html', {'tx_ref': request.user.username + '-' + str(tx_ref)})
        # farmer.subscription = Subscription.objects.create(tx_ref=request.user.username + '-' + str(tx_ref))
        farmer.save()

def subscription_activator(request):
    # trx_ref = request.GET.get('trx_ref')
    # if trx_ref is not None:
    #     print('Hellloooooo')
    #     subcription = Subscription.objects.get(tx_ref=trx_ref)
    #     if subcription is not None:
    #         print(trx_ref)
    #         print(subcription)
    farmer = request.user.profile
    subscription = farmer.subscription.first()
    if subscription is not None:
        subscription.date = timezone.now()
        subscription.save()
    else:
        subscription = Subscription.objects.create(farmer=farmer, date=timezone.now())
        subscription.save()
    messages.success(request, f'Successfully Subscribed')
    return redirect('profile-page')

def subscripiton_verifier(request, pk):
    pass