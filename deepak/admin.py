from django.contrib import admin
from .models import BloodRequest


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'blood_group',
        'units',
        'hospital',
        'needed_date',
        'created_at',
    )
    list_filter = ('blood_group', 'needed_date', 'created_at')
    search_fields = ('full_name', 'phone', 'email', 'hospital')
    readonly_fields = ('created_at',)
