from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'sex',
            'email',
            'contact_number',
            'password',
            'password2',
            # 'profile_pic',
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'sex',
            'email',
            'contact_number',
            'password',
            # 'password2',
            # 'profile_pic',
        )


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password')