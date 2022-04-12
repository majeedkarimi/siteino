from django import forms  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate

  

  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class UserLoginForm(forms.Form):
        username=forms.CharField(max_length=40)
        password=forms.CharField(max_length=40,widget=forms.PasswordInput)


        def clean(self,*args,**kwargs):
            username=self.cleaned_data.get("username")
            password=self.cleaned_data.get("password")
            user_qs = User.objects.filter(username=username)
            if user_qs.count() == 0:
                raise forms.ValidationError("The user does not exist")
            else:
                if username and password:
                     user = authenticate(username=username, password=password)

                     if not user:
                        raise forms.ValidationError(u"Incorrect password")
                     if not user.is_active:
                         raise forms.ValidationError(u"This user is no longer active")
            return super(UserLoginForm,self).clean(*args,**kwargs)
