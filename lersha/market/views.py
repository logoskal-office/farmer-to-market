from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category
from django.core.paginator import Paginator
import random
import users

from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

def product_list(request):
    products = Product.objects.order_by('-id')
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
        'market/product-list.html',
        {
            'products': products_page, 
            'categories': categories,
            'querystring': querydict.urlencode(),
        }
    )

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.impressions.create(time=timezone.now())
    
    return render(request, 'market/product-detail.html', {'product':product})