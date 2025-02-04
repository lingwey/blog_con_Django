from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown

register = template.Library()
@register.simple_tag
def total_post():
    return Post.manage_perso.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts= Post.manage_perso.order_by('-publicacion')[:count]
    return {'latest_posts': latest_posts}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
