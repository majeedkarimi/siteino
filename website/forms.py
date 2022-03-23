from django.forms import ModelForm
from website.models import Contact,Newsletter

class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class NewsletterModelForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'