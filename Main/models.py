# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import title

## Цитата.
class Quotations(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название цитаты')

    text = models.TextField(verbose_name='Текст цитаты')
    
    author = models.ForeignKey('Author', verbose_name='Автор')
    
    def __unicode__(self):
        return self.title;
    
    def __str__(self):
        return str(self.id)
    

class Videos (models.Model):
    title = models.CharField(max_length=100, verbose_name='Название видео')
    
    url = models.TextField(verbose_name='Ссылка на видео')
    
    picture = models.TextField(verbose_name='Ссылка на картинку')
    
    def __unicode__(self):
        return self.title;
    
    def __str__(self):
        return self.title
    
    def get_picture(self):
        return 'img/videos/' + self.picture
    
    
## Книга
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    text = models.TextField(verbose_name='Описание книги')
    
    picture = models.CharField(max_length=100, verbose_name='Обложка книги')
    
    prize = models.IntegerField(verbose_name='Цена')
    
    genre = models.ForeignKey('Genre', verbose_name='Жанр')
    
    publishing = models.ForeignKey('Publishing',verbose_name='Издательство')
    
    author = models.ForeignKey('Author', verbose_name='Автор')
    
    ## Возвращает url страницу книги.
    def get_absolute_url(self):
        return '/book/%i/' % self.id
  
    ## Возвращает путь до обложки книги.
    def get_picture(self):
        return 'img/books/' + self.picture

    def __unicode__(self):
        return self.title;
    
    def __str__(self):
        return str(self.title)
    
## Заказ.   
class Order(models.Model):
    
    
    date = models.DateField(verbose_name='Дата')
    
    time = models.TimeField(verbose_name='Время')
    
    user = models.ForeignKey(User, verbose_name='Пользователь')
    
    status = models.ForeignKey('Status', verbose_name='Статус заказа')
    
    def __unicode__(self):
        return 'Заказ номер ' + self.id;
    
    def __str__(self):
        return str(self.id)
    
## Сущность с товаром и его количеством в заказе.
class OrderProduct(models.Model):
    
    numbers = models.IntegerField(verbose_name='Количество товара')
    
    product = models.ForeignKey('Book', verbose_name='Товар')
    
    order = models.ForeignKey('Order', verbose_name='Заказ')
    
    def __unicode__(self):
        return 'Товар номер ' + self.id;
    
    def __str__(self):
        return str(self.id)

## Рецензия.
class Review(models.Model):
    
    text = models.TextField(verbose_name='Текст рецензии')
    
    user = models.ForeignKey(User, verbose_name='Автор')
    
    product = models.ForeignKey('Book', verbose_name='Товар')
    
    def __unicode__(self):
        return 'Рецензия номер ' + self.id;
    
    def __str__(self):
        return self.text
        
## Жанр.
class Genre(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Название')
    
    def __unicode__(self):
        return self.title;
    
    def __str__(self):
        return self.title
    
## Издательство.
class Publishing(models.Model):
    
    text = models.TextField(verbose_name='Описание')
    
    title = models.CharField(max_length=100, verbose_name='Название')
    
    picture = models.CharField(max_length=100, verbose_name='Изображение')
    
    def __unicode__(self):
        return self.title;
    
    def __str__(self):
        return self.title
    
    ## Возвращает url страницу издательства.
    def get_absolute_url(self):
        return '/publishing/%i/' % self.id
    
    ## Возвращает путь до изображения издательства.
    def get_picture(self):
        return 'img/publishings/' + self.picture

## Автор.    
class Author(models.Model):
    
    personalData = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    
    text = models.TextField(verbose_name='Описание/Биография')
    
    picture = models.CharField(max_length=100, verbose_name='Изображение')
    
    def __unicode__(self):
        return self.personalData;
    
    def __str__(self):
        return self.personalData;
    
    ## Возвращает url станицу автора.
    def get_absolute_url(self):
        return '/author/%i/' % self.id
    
    ## Возвращает путь до изображения автора.
    def get_picture(self):
        return 'img/authors/' + self.picture
    
## Для разработки других категорий (не только книги).
class Category(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Название')
    
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title;

## Статус заказа. Текущий, Отложенный или Выполненый. В разработке.
class Status(models.Model):
    
    class Meta:
        verbose_name_plural = "Statuses"
    
    title = models.CharField(max_length=20, verbose_name='Описание')
    
    def __str__(self):
        return str(self.id) + " " + self.title
    
    def __unicode__(self):
        return self.title;

