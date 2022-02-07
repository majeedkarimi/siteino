from django.shortcuts import render

# Create your views here.


def index_blog(request):
    return render(request, 'blog/blog-home.html')


def single_blog(request):
    return render(request, 'blog/blog-single.html')