from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm

from .models import ManagerUser


class ManagerUserForm(forms.ModelForm):
    
    class Meta:
        model = ManagerUser
        fields = '__all__'
        exclude = ('groups', 'user_permissions')  


class ManagerUserUpdateForm(forms.ModelForm):
    class Meta:
        model = ManagerUser
        fields = '__all__' 
        exclude = ( 'groups',
                    'user_permissions' )

class ManagerUserLoginForm(forms.Form):
    
    dni = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    exclude = ('groups', 'user_permissions') 


