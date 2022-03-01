from django.shortcuts import render
from blog.models import Post
# Create your views here.


def index_blog(request):
    posts = Post.objects.filter(status=1)
    content = {'posts':posts}
    return render(request, 'blog/blog-home.html',content)


def single_blog(request):
    return render(request, 'blog/blog-single.html')