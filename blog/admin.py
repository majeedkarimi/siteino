from django.contrib import admin
from blog.models import Post,Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title','content','counted_views','status')
    list_display = ('title','author','pk','status','created_date',
                    'updated_date','published_date')
    list_filter = ('status','author')
    search_fields = ('title','content',)
    # ordering = ["-created_date"]
    summernote_fields = ('content',)
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category)