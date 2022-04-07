from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# login by html login form.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/contact')
    elif request.method == 'GET':
        return render(request,'accounts/login.html')
    elif request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            next= request.POST.get('next')
            print(next)
            user=authenticate(request, username=username, password=password)
            if user is not None and next is None: 
                login(request, user)
                return redirect('/about')
            elif user is not None and next is not None:
                login(request, user)
                return redirect(next)
        else:
            return render(request,'accounts/login.html')


# login by django auth forms
# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'GET':
#         form = AuthenticationForm()
#         content={'form':form}
#         return render(request,'accounts/login.html',content)
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request,data=request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get('username')
#             password=form.cleaned_data.get('password')
#             user=authenticate(request, username=username, password=password)
#             if user is not None: 
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 print('user not found')
#         else:
#             return render(request,'accounts/login.html',{'form': form})
    
    
    
@login_required 
def logout_view(request):
    logout(request)    
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')
        return render(request,'accounts/signup.html')
    else:
        return redirect('/')




