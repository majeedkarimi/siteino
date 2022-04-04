from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# login by html login form.
# def login_view(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/') 
#     return render(request,'account/login.html',content)


# login by django auth forms
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        form = AuthenticationForm()
        content={'form':form}
        return render(request,'account/login.html',content)
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
            return render(request,'account/login.html',{'form': form})
    
    
    
    
# def logout_view(request):
#     return 

def signup_view(request):
    return render(request,'account/signup.html')