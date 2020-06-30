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

@register.simple_tag
def maxpoint(value1, value2, value3, value4, value5):
    return max(value1, value2, value3, value4, value5)

@register.simple_tag
def minpoint(value1, value2, value3, value4, value5):
    return min(value1, value2, value3, value4, value5)

@register.simple_tag
def embupoint(value1, value2, value3, value4, value5, value6, value7):
    return value1 + value2 + value3 + value4 + value5 - value6 - value7
