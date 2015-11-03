from django import template

register = template.Library()

## Отображает список товаров в корзине.
# @param order_product Сущность с товаром и его количеством.
@register.inclusion_tag('product_order_object.html')
def get_products_in_basket(order_product):
    product = order_product.product
    numbers = order_product.numbers
    return {'product': product, 'numbers': numbers,
            'order_product_id': order_product.id}