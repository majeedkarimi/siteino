from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from blog.models import Post
from django.db.models.functions import Now
from website.forms import ContactModelForm,NewsletterModelForm
from django.contrib import messages

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
            messages.success(request,'your email submited successfully')
            # messages.add_message(request.SUCCESS,'your email submited successfully')
        else:
            messages.error(request,'your message didnt submited')
        
    return render(request,'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

