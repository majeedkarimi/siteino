from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.models import SignupForm
   
# # login by html login form.
# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('/')
#     elif request.method == 'GET':
#         return render(request,'accounts/login.html')
#     elif request.method == 'POST':
#         # form = AuthenticationForm(request=request,data=request.POST)
#         # if form.is_valid():
#             # username=form.cleaned_data.get('username')
#             # password=form.cleaned_data.get('password')
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         next= request.POST.get('next')
#         username1=''
#         email1=''
#         if '@' in username:
#             email1 = username
#         else:
#             username1 = username
#         if username1:
#             try:
#                 user = User.objects.get(username__iexact=username1)
#                 print(user.check_password(password))
#                 if user.check_password(password) == False:
#                     user = None
#             except User.DoesNotExist:
#                 return render(request,'accounts/login.html')
#         elif email1:
#             try:
#                 user = User.objects.get(email__iexact=email1)
#                 if user.check_password(password) == False:
#                     user = None
#             except User.DoesNotExist:
#                 return render(request,'accounts/login.html')
#         # user=authenticate(request, username=username, password=password)
#         if user is not None and next=='': 
#             login(request, user)
#             return redirect('/')
#         elif user is not None and next!='':
#             login(request, user)
#             return redirect(next)
#         else:
#             return render(request,'accounts/login.html')

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailOrUsernameModelBackend(ModelBackend):
    """
    This is a ModelBacked that allows authentication
    with either a username or an email address.
    
    """
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, username):
        try:
            return get_user_model().objects.get(pk=username)
        except get_user_model().DoesNotExist:
            return None

# login with auth
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'GET':
        return render(request,'accounts/login.html')
    elif request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        remember_me = request.POST.get('remember')
        print(remember_me)
        next= request.POST.get('next')
        user=EmailOrUsernameModelBackend.authenticate(request, username=username, password=password)
        
        if user is not None and next=='': 
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0) 
            return redirect('/')
        elif user is not None and next!='':
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0) 
            return redirect('/')
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


# def signup_view(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form=UserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('/accounts/login')
#         return render(request,'accounts/signup.html')
#     else:
#         return redirect('/')
    

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')
        return render(request,'accounts/signup.html')
    else:
        return redirect('/')




