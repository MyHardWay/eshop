import datetime
import json  

from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound, HttpResponse   

from Main.models import Author, Book, Genre, Order, OrderProduct, Publishing
from Main.models import Status

## Отображает стартовую страницу сайта.
def show_index_page(request):
    res_dict = make_res_dict(request)
    res_dict.update(csrf(request))
    books = Book.objects.all()[:5]
    res_dict['products'] = books
    return render_to_response ('index.html', res_dict)

## Отображает страницу корзины пользователя.
def show_basket_page(request):
    if request.user.is_authenticated():
        res_dict = make_res_dict(request)
        ## Статус id = 1, когда заказ формируется.
        order = Order.objects.filter(user=request.user,
                                    status=Status.objects.get(id=1))
        if order:
            order_products = OrderProduct.objects.filter(order=order)
        else:
            order_products = []
        res_dict['order_products'] = order_products  
        return render_to_response ('basket.html', res_dict)
    return HttpResponseNotFound('<h1>Page not found</h1>')
    
## Отображает страницу с информацией о книге.
# @param book_id ИД книги.   
def show_book_info_page(request, book_id):
    book = Book.objects.get(id=book_id)
    res_dict = make_res_dict(request)
    res_dict['product'] = book
    return render_to_response ('product_info.html',res_dict)
    
## Отображает страницу с результатами поиска по сайту.
# @param search_val Параметры поиска.    
def show_search_page(request, search_val):
    res_dict = make_res_dict(request)
    res_dict['books'] = Book.objects.filter(title__icontains=search_val)
    res_dict['authors'] = Author.objects.filter(
                            personalData__icontains=search_val)
    res_dict['publishings'] = Publishing.objects.filter(
                                title__icontains=search_val)
    return render_to_response ('search.html', res_dict)
    
## Добавляет товар в корзину.   
def make_purchase(request):
    if request.method == "POST":
        if request.is_ajax:
            # Если пользователь авторизован, то добавляет товар в корзину,
            # иначе переходит на страницу регистрации.
            if request.user.is_authenticated():
                product_id = request.POST['id']
                cur_product = Book.objects.get(id=product_id)
                cur_order = Order.objects.filter(user=request.user, 
                                            status=Status.objects.get(id=1))
                # Если уже есть формирующийся заказ, то добавляет товар туда.
                if cur_order:
                    # Если такой продукт уже есть в корзине, то увеличивает
                    # их колличество.
                    order_product = OrderProduct.objects.filter(
                                        order=cur_order[0], 
                                        product=cur_product)
                    if order_product:
                        order_product[0].numbers += 1
                        order_product[0].save()
                    # Иначе создаёт новую сущность.
                    else:                     
                        order_product = OrderProduct(
                                            product=cur_product,
                                            order=cur_order[0], numbers=1)
                        order_product.save()
                # Иначе создаёт новый заказ.
                else:
                    cur_status = Status.objects.get(id=1)
                    new_order = Order(user=request.user, status=cur_status,
                                date=datetime.date.today(),
                                time=datetime.time())
                    new_order.save()
                    order_product = OrderProduct(product=cur_product,
                                        order=new_order, numbers=1)
                    order_product.save()
                return HttpResponse(json.dumps({'result': 'success'}))
            else:
                return HttpResponse(json.dumps({'result': 'redirect'}))
        else:
            return HttpResponse(json.dumps({'result': 'fail'}))
    return HttpResponse(json.dumps({'result': 'error'}))

## Отображает страницу автора книги.
# @param author_id ИД автрора.
def show_author_info_page(request, author_id):
    res_dict = make_res_dict(request)
    cur_author = Author.objects.get(id=author_id)
    res_dict['content'] = cur_author
    return render_to_response ('about.html', res_dict)

## Отображает страницу издательства.
# @param publishing_id ИД издательства.   
def show_publishing_info_page(request, publishing_id):
    res_dict = make_res_dict(request)
    cur_publishing = Publishing.objects.get(id=publishing_id)
    res_dict['content'] = cur_publishing
    return render_to_response ('about.html', res_dict)

## Удаляет товар из корзины.    
def delete_order_product(request):
    if request.method == "POST":
        if request.is_ajax:
            order_product_id = request.POST['product_order_id']
            cur_order_product = OrderProduct.objects.filter(
                                    id=order_product_id)
            if cur_order_product:
                cur_order_product.delete()
                return HttpResponse(json.dumps({'result': 'success'}))
            return HttpResponse(json.dumps({'result': 'fail'}))

## Отображает страницу книгами принадлежащими указаному жанру.
# @param genre_id ИД жанра.       
def show_book_of_selected_genre(request, genre_id):
    res_dict = make_res_dict(request)
    cur_genre = Genre.objects.filter(id=genre_id)[0]
    products = Book.objects.filter(genre=cur_genre)
    res_dict['products'] = products 
    return render_to_response ('genre.html', res_dict)

## Создаёт словарь с текущим пользователем, и жанрами.    
def make_res_dict(request):
    res_dict = {}
    res_dict['username'] = auth.get_user(request).username
    res_dict['genres'] = Genre.objects.all()
    return res_dict
