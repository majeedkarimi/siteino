from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# login by html login form.
# def login_view(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/') 
#     return render(request,'accounts/login.html',content)


# login by django auth forms
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        form = AuthenticationForm()
        content={'form':form}
        return render(request,'accounts/login.html',content)
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('/')
            else:
                print('user not found')
        else:
            return render(request,'accounts/login.html',{'form': form})
    
    
    
@login_required 
def logout_view(request):
    logout(request)    
    return redirect('blog:index')


def signup_view(request):
    return render(request,'accounts/signup.html')