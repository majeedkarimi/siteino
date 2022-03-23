from django.contrib import admin
from website.models import Contact,Newsletter
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # ordering = ['-created_date']
    list_filter = ['email']
    empty_value_display = '-empty-'
    list_display = ['name','email','created_date']
    search_fields = ['message','subject']
admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)