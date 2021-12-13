from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    models = MyUser
    list_display = ['pk', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'gender', 'address', 'profile_img',)}),

    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'address', 'profile_img',)}),
    )

admin.site.register(MyUser, CustomUserAdmin)