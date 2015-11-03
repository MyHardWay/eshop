from django import template

register = template.Library()

## Отображает список товаров. 
# @param book Товар.
@register.inclusion_tag('product_add_object.html')
def get_product(product):
    return {'product': product}
    
    

    
    