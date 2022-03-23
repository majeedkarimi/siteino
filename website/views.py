from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from blog.models import Post
from django.db.models.functions import Now
from website.forms import ContactModelForm,NewsletterModelForm

def index_view(request):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(published_date__lte=Now())
    latest = posts[:6]
    content = {"latest_posts":latest}
    return render(request,'website/index.html',content)


def about_view(request):
    return render(request,'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request,'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

