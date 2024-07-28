from django import template
import footballers.views as views
from footballers.models import Category,TagPost
from django.db.models import Count

register = template.Library()



@register.inclusion_tag('footballers/list_categories.html')
def show_categories(cat_selected = 0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {'cats':cats,'cat_selected':cat_selected}



@register.inclusion_tag('footballers/list_tags.html')
def show_all_tegs():
    return {'tags':TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}