from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm

from .models import AigasraUser


class AigasraUserForm(forms.ModelForm):
    
    class Meta:
        model = AigasraUser
        fields = '__all__'
        exclude = ('groups', 'user_permissions')  


class AigasraUserUpdateForm(forms.ModelForm):
    class Meta:
        model = AigasraUser
        fields = '__all__' 
        exclude = ( 'groups',
                    'user_permissions' )

class AigasraUserLoginForm(forms.Form):
    
    dni = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    exclude = ('groups', 'user_permissions') 


