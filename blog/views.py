from django.shortcuts import get_object_or_404, render
from blog.models import Post
import datetime
from django.db.models.functions import Now
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


# def index_blog(request,cat_name=None,author_username=None):
#     posts = Post.objects.filter(status=1)
#     # current_datetime = datetime.datetime.now()
#     # posts = posts.filter(published_date__lte=current_datetime)
#     posts = posts.filter(published_date__lte=Now())
#     posts = posts.order_by('published_date')
#     if cat_name != None:
#         posts = posts.filter(category__name=cat_name)
#     if author_username != None:
#         posts = posts.filter(author__username=author_username)
#     content={'posts':posts}
#     return render(request, 'blog/blog-home.html',content)

def index_blog(request,**kwargs):
    posts = Post.objects.filter(status=1)
    # current_datetime = datetime.datetime.now()
    # posts = posts.filter(published_date__lte=current_datetime)
    posts = posts.filter(published_date__lte=Now())
    posts = posts.order_by('-published_date')
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs.get('cat_name'))
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs.get('author_username'))
    paginator = Paginator(posts,3)
    try:
        number_page = request.GET.get('page')
        posts = paginator.page(number_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    content={'posts':posts}
    return render(request, 'blog/blog-home.html',content)

    
def single_blog(request,id):
    update_views = Post.objects.get(pk=id)
    update_views.counted_views += 1
    update_views.save()
    posts = Post.objects.filter(status=1)
    posts = posts.filter(published_date__lte=datetime.datetime.now())
    posts = get_object_or_404(posts, pk=id)
    
    
    view_post = Post.objects.filter(status=1)
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    view_post = view_post.filter(published_date__lte=current_datetime)
    view_post = view_post.order_by('-published_date')
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

def search_blog(request):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(published_date__lte=Now())
    posts = posts.order_by('published_date')
    if s := request.GET.get('s'): #walrus oprator
        posts=posts.filter(content__contains=s)
    content={'posts':posts}
    return render(request, 'blog/blog-home.html',content)