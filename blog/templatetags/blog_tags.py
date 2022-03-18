from django import template

register = template.Library()

from blog.models import Post

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(args):
    posts=Post.objects.filter(status=1).order_by('-published_date')[:args]
    return {"posts":posts}