from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    sector = forms.CharField(max_length=100, required=True)
    name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'name','email', 'sector', 'password1', 'password2')

class ChangePassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ProfilePageForm(UserChangeForm):
    email = forms.EmailField(required=True)
    sector = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'sector')

class UserEditForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    sector = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'sector', 'is_active', 'is_staff', 'is_superuser']