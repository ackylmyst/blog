from django import forms
from .models import User, Role

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'first_name', 'last_name', 'age', 'role']
        labels = {
            'login': 'Login',
            'password': 'Password',
            'first_name': 'First name',
            'last_name': 'Last name',
            'age': 'Age',
            'role': 'Role'
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['title']
        labels = {
            'title': 'Title',
        }