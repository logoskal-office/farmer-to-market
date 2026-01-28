from django.db import models
from authentication.models import LershaUser
from market.models import Product, Impression, Contact
from .validators import phone_number_validator
from django.utils import timezone
from datetime import timedelta

class Farmer(models.Model):
    account = models.OneToOneField(LershaUser, null=True, blank=True, related_name='profile',on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/users/' ,null=True, blank=True)
    phone_number = models.CharField(max_length=9, validators=[phone_number_validator])
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey('City', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True, blank=True, max_length=1000)

    def calculate_impressions(self, range=30):
        date_difference = timezone.now() - timedelta(days=range)
        return Impression.objects.filter(product__farmer=self, time__gte=date_difference).count()

    def calculate_contacts(self, range=30):
        date_difference = timezone.now() - timedelta(days=range)
        return Contact.objects.filter(product__farmer=self, time__gte=date_difference).count()
    
    def get_name(self):
        return self.account.first_name + ' ' + self.account.last_name
    
    def __str__(self):
        return f"{self.account.first_name if self.account else ''} {self.account.last_name if self.account else ''} ({self.id})"

    def is_active(self):
        if self.account.is_active:
            if self.subscription.exists():
                subscription = self.subscription.first()
                if subscription.date + timedelta(days=30) > timezone.now():
                    return True
        return False


class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey('State', related_name='cities', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    farmer = models.ForeignKey(Farmer, related_name='subscription', on_delete=models.CASCADE)
    date = models.DateField()
    