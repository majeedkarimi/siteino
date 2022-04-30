from django.shortcuts import render
from comingsoon.forms import ComingsoonModelForm
from django.shortcuts import render
from django.contrib import messages

def splashview(request):
    if request.method=="POST":
        form = ComingsoonModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'The email was successfully submitted')
        else:
            messages.error(request,'There was a problem registering the comment')
            
    form=ComingsoonModelForm()
    content = {'form':form}
    return render(request, 'comingsoon.html',content)
