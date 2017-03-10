from django.contrib import admin
from .models import Book, Genre, Publishing, Author, Category, Order
from .models import Topics, OrderProduct, Status, Videos

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Publishing)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Status)
admin.site.register(Topics)
admin.site.register(Videos)
