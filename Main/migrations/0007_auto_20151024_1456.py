# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_auto_20151023_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publishing',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
