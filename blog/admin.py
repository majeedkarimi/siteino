from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title','content','counted_views','status')
    list_display = ('title','author','pk','status','login_require','created_date',
                    'updated_date','published_date')
    list_filter = ('status','author')
    search_fields = ('title','content',)
    # ordering = ["-created_date"]
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('title','content','counted_views','status')
    list_display = ('name','post','subject','created_date','updated_date')
    list_filter = ('approved','name')
    search_fields = ('subject','message',)
    
admin.site.register(Comment,CommentAdmin)   
admin.site.register(Post,PostAdmin)
admin.site.register(Category)