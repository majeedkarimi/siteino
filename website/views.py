from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from blog.models import Post
from django.db.models.functions import Now

def index_view(request):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(published_date__lte=Now())
    latest = posts[:6]
    content = {"latest_posts":latest}
    return render(request,'website/index.html',content)


def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    return render(request,'website/contact.html')
