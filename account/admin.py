from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

# admin.site.register(User)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (_('Личная информация'), {'fields' : ('username', 'first_name', 'last_name', 'phone')}),
        (_('Данные для авторизации'), {'fields': ('email', 'password')}),
        (_('Доступ'), {'fields' : ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Доп. Инфо'), {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'usable_password', 'password1', 'password2')
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    readonly_fields = ('date_joined', 'last_login')

admin.site.register(User, CustomUserAdmin)