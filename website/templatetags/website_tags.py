from django import template
from django.core.paginator import Paginator
register = template.Library()

@register.inclusion_tag('website/latest_posts.html', takes_context=True)
def latest_posts(context):
    latest_posts = context['latest_posts']
    return {"latest_posts":latest_posts}
    