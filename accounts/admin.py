from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserForm, CustomUserChangeForm
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','contact_number']

admin.site.register(CustomUser, CustomUserAdmin)