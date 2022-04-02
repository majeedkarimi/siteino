from django.forms import ModelForm
from blog.models import Comment
from captcha.fields import CaptchaField

class CommentModelForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Comment
        fields = '__all__'


        