from django.contrib import admin
from .models import Farmer, City, State, Subscription

admin.site.register(Farmer)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Subscription)