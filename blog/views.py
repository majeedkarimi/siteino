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
    posts = Post.objects.filter(status=1)
    posts = posts.filter(published_date__lte=datetime.datetime.now())
    posts = get_object_or_404(posts, pk=id)
    
    
    view_post = Post.objects.filter(status=1)
    current_datetime = datetime.datetime.now()
    view_post = view_post.filter(published_date__lte=current_datetime)
    view_post = view_post.order_by('published_date')
    list_view_post = list(view_post)
    post_count = len(list_view_post)
    post_index = list_view_post.index(Post.objects.get(pk=id))
    if post_count==1 :
        prev_post = None
        next_post = None
    elif post_count==2:
        if post_index==0:
            prev_post = None
            next_post = list_view_post[1]
        elif post_index==1:
            prev_post = list_view_post[0]
            next_post = None
    elif post_count>2:
        if post_index == post_count-1:
            prev_post = list_view_post[post_count-2]
            next_post = None
        elif post_index == 0:
            prev_post = None
            next_post = list_view_post[1]
        elif post_index>0 and post_index<post_count-1:
            prev_post = list_view_post[post_index-1]
            next_post = list_view_post[post_index+1]

    content = {'posts':posts,'next':next_post,'prev':prev_post}
    return render(request, 'blog/blog-single.html',content)