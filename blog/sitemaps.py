from django.contrib.sitemaps import Sitemap
from blog.models import Post
import datetime
from django.urls import reverse

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        posts = Post.objects.filter(status=1)
        posts = posts.filter(published_date__lte=datetime.datetime.now())
        return posts

    def lastmod(self, obj):
        return obj.updated_date
    
    def location(self, item):
        return reverse('blog:single',kwargs={'id':item.id})
        