from django import forms  
from user.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
class UserForm(UserCreationForm):

    
    class Meta:
        model = get_user_model()
        fields = {'full_name','username','password1','password2'}