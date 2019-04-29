from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from backend import models


@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    """
    Extend the base Django UserAdmin with support for some Buza fields.
    """

    date_hierarchy = 'date_joined'
    ordering = ['-date_joined']
    list_display = list(DjangoUserAdmin.list_display) + ['date_joined']
