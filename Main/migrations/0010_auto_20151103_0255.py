# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0009_auto_20151103_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='userId',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(verbose_name='Автор', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='personalData',
            field=models.CharField(max_length=100, verbose_name='Ф.И.О.'),
        ),
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.CharField(max_length=100, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='author',
            name='text',
            field=models.TextField(verbose_name='Описание/Биография'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(verbose_name='Автор', to='Main.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(verbose_name='Жанр', to='Main.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.CharField(max_length=100, verbose_name='Обложка книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='prize',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing',
            field=models.ForeignKey(verbose_name='Издательство', to='Main.Publishing'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.TextField(verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(verbose_name='Статус заказа', to='Main.Status'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='order',
            name='userId',
            field=models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='numbers',
            field=models.IntegerField(verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(verbose_name='Заказ', to='Main.Order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(verbose_name='Товар', to='Main.Book'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='picture',
            field=models.CharField(max_length=100, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='text',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='publishing',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(verbose_name='Товар', to='Main.Book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Текст рецензии'),
        ),
    ]
