from django.contrib import admin
from comingsoon.models import Notify_Me
# Register your models here.

class CommingsoonAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # ordering = ['-created_date']
    list_filter = ['email']
    empty_value_display = '-empty-'
    list_display = ['email','created_date']
    search_fields = ['email']
admin.site.register(Notify_Me,CommingsoonAdmin)

