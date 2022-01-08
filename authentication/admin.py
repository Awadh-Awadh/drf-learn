from django.contrib import admin
from authentication.models import CustomUser
from helpers.models import TrackingModel
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChange, CustomUserCreation


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChange
    model= CustomUser

admin.site.register(CustomUser, CustomUserAdmin)