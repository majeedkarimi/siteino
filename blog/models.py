from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    tag = TaggableManager()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"({self.id}) {self.title}"
    
    class Meta:
        ordering =['-published_date']

    # def truncate_string(self):
    #     return self.content[:100]+" ... "
    
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'id':self.id})
