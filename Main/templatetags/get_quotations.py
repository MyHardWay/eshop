from django import template

register = template.Library()

## Отображение цитаты. 
# @param quotation Цитата.
@register.inclusion_tag('quotations.html')
def get_quotations(quotation):
    return {'quotation': quotation}
    