from django.contrib import admin

from .models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = (
        'customer', 'start_date', 'end_date', 'classification', 'rating'
    )

admin.site.register(Trip, TripAdmin)
