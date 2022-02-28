from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=300)
    content = models.TextField()
    # category
    # tag
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    cretaed_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
