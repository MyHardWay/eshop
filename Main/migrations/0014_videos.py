# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-20 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_auto_20170217_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название видео')),
                ('url', models.TextField(verbose_name='Ссылка на видео')),
            ],
        ),
    ]
