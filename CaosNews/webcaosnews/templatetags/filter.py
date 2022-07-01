from django import template

register = template.Library()


@register.filter(name='split')
def split(value, key):
    """
      Returns the value turned into a list.
    """
    return value.split(key)

@register.filter
def to_char(value):
    return chr(98+value)