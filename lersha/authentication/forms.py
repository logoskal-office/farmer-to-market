from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import LershaUser

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = LershaUser
        fields = ["username", "email", "password", "first_name", "last_name", "phone_number"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full px-4 py-3 rounded-lg border border-primary-300 focus:ring-2 focus:ring-primary-500'
            })
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # 🔐 hash it
        if commit:
            user.save()
        return user