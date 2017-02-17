'''
Created on 24 авг. 2015 г.

@author: way
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_index_page, name='index_page'),
    url(r'^basket/$', views.show_basket_page, name='basket_page'),
    url(r'^search/$', views.show_search_page,
        name='search_page'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.show_book_info_page, 
        name='book_info_page'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.show_author_info_page,
        name='author_info_page'),
    url(r'^publishing/(?P<publishing_id>[0-9]+)/$', views.show_publishing_info_page,
        name='publishing_info_page'),
    url(r'^makepurchase/$', views.make_purchase),
    url(r'^delete-order-product/$', views.delete_order_product),
    url(r'^genre/$', views.show_book_of_selected_genre,
        name='book_of_selected_genre'),
]