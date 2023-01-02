from django.contrib import admin
from django import forms
from django.contrib.auth.forms import AdminPasswordChangeForm

from .models import User

class UserChangeForm(forms.ModelForm):
    password = AdminPasswordChangeForm

    class Meta:
        model = User
        fields = ('password',)

class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    list_display = (
    'username',
    'first_name',
    'last_name',
    'email',
    'role',
)

admin.site.register(User, UserAdmin)
