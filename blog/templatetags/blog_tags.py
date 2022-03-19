from django import template
from django.contrib.auth.models import User
register = template.Library()

from blog.models import Post,Category
from django.db.models import Count

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(args):
    posts=Post.objects.filter(status=1).order_by('-published_date')[:args]
    return {"posts":posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    categories = Category.objects.filter(post__status=1).annotate(Count("post"))
    return {"categories":categories}

@register.inclusion_tag('blog/blog_athor.html')
def authors():
    authors = User.objects.all()
    return {"authors":authors}