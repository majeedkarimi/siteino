from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title','content','counted_views','status')
    list_display = ('title','content','status','created_date',
                    'updated_date')
    list_filter = ('status',)
    search_fields = ('title','content',)
    # ordering = ["-created_date"]
    
admin.site.register(Post,PostAdmin)