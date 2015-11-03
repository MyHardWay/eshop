# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_auto_20151024_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publishing',
            name='picture',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
