from django import template
from core.unsplash import get_iotd

register = template.Library()

@register.simple_tag
def get_random_image():
    url = get_iotd()
    return url