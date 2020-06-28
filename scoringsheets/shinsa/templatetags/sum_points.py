from django import template
register = template.Library()

@register.simple_tag
def points(value1, value2, value3, value4, value5):
    return value1 + value2 + value3 + value4 + value5

@register.simple_tag
def success():
    return "success"

@register.simple_tag
def failure():
    return "failure"
