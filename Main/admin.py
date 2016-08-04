from django.contrib import admin
from .models import Book, Genre, Publishing, Author, Category, Order, OrderProduct, Status

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Publishing)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Status)
