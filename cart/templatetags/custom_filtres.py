from django import template

register = template.Library()


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
