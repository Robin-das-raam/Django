from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    confirm_password = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email']

    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("password dont match")

        return confirm_password