from django.shortcuts import render, redirect
from django.contrib import messages
from uuid import uuid4
from .models import Farmer
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from users.models import State, City
from .forms import FarmerUpdateForm, FarmerUserUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = FarmerUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        form_user = FarmerUserUpdateForm(request.POST, instance=request.user)
        if form_user.is_valid():
            if form.is_valid():
                form.save()
                form_user.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile-page')
            else:
                print(form.errors)
        else:
            print(form_user.errors)
            form = FarmerUpdateForm(instance=request.user.profile)
    context = {'cities': City.objects.all(), 'states': State.objects.all()}
    return render(request, 'users/profile.html', context=context)

# def subcribe(request):
#     tx_ref = uuid4()
#     farmer = request.user.profile.first()
#     if farmer.subscription is None:
#         farmer.subscription = Subscription.objects.create(tx_ref=request.user.username + '-' + str(tx_ref))
#         farmer.save()
#         print(farmer.subscription.is_subscribed())
#         return render(request, 'users/subscribe.html', {'tx_ref': request.user.username + '-' + str(tx_ref)})
#     else:
#         pass

# def subscription_activator(request):
#     trx_ref = request.GET.get('trx_ref')
#     if trx_ref is not None:
#         print('Hellloooooo')
#         subcription = Subscription.objects.get(tx_ref=trx_ref)
#         if subcription is not None:
#             print(trx_ref)
#             print(subcription)
#             subcription.subscription_date = timezone.now()
#             subcription.save()
#             messages.success(request, f'Successfully Subscribed')
#     return redirect('profile-page')