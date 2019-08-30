from ..models import Artical, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_articals(num=5):
    return Artical.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    return Artical.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

