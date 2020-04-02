from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Customer


class CustomerAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'email',
                'password1',
                'password2'
            ),
        }),
    )

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password'
            )
        }),
        (_('Personal info'), {
            'fields': (
                'name',
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_staff',
                'is_superuser',
                'is_active',
            )
        }),
        (_('Important dates'), {
            'fields': (
                'last_login',
            )
        }),
    )

    list_display = (
        'email',
        'name',
    )

    list_filter = (
        'groups',
    )

    search_fields = (
        'name',
        'email'
    )

    ordering = ('-id',)



admin.site.register(Customer, CustomerAdmin)
