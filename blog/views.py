from django.shortcuts import get_object_or_404, render
from blog.models import Post
import datetime
# Create your views here.


def index_blog(request):
    posts = Post.objects.filter(status=1)
    current_datetime = datetime.datetime.now()
    posts = posts.filter(published_date__lte=current_datetime)
    posts = posts.order_by('published_date')
    content = {'posts':posts,}
    return render(request, 'blog/blog-home.html',content)


def counter_views(id):
    update_views = Post.objects.get(pk=id)
    update_views.counted_views = update_views.counted_views+1
    update_views.save()
    
def single_blog(request,id):
    counter_views(id)
    posts=get_object_or_404(Post,pk=id)
    content = {'posts':posts}
    return render(request, 'blog/blog-single.html',content)