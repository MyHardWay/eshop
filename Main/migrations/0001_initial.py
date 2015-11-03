# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Название', max_length=255)),
                ('announce', models.CharField(blank=True, verbose_name='Анонс', max_length=255)),
                ('date', models.DateField(verbose_name='Дата')),
                ('date_end', models.DateField(null=True, blank=True, verbose_name='Дата до')),
            ],
            options={
                'verbose_name_plural': 'События',
                'verbose_name': 'Событие',
            },
        ),
    ]
