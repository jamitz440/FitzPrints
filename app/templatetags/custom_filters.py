from django import template

register = template.Library()

@register.filter
def remove_hex(value):
    import re
    return re.sub(r'\s\w{6}$', '', value)