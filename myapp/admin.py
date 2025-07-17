from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'category', 'submitted_at')
    list_filter = ('category', 'gender', 'submitted_at')
    search_fields = ('user_name', 'user_email', 'user_phone')

