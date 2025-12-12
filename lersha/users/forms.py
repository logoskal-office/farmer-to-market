from django.forms import ModelForm
from .models import Farmer
from authentication.models import LershaUser

class FarmerUpdateForm(ModelForm):
# Must only try to update the specified fields and not all fields
    class Meta:
        model = Farmer
        fields = ['phone_number', 'address', 'city']

class FarmerUserUpdateForm(ModelForm):
    class Meta:
        model = LershaUser
        fields = ['first_name', 'last_name', 'email']