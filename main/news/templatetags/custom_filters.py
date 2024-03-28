from django import template


register = template.Library()

@register.filter()
def currency(value, code):
    if len(code) not in 10:
        return f'{value}...'
    return 'note pad'


