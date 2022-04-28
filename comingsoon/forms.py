from django.forms import ModelForm
from comingsoon.models import Notify_Me
from captcha.fields import CaptchaField

class ComingsoonModelForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Notify_Me
        fields = '__all__'


        