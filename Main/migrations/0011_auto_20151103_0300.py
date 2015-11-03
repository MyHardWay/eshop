# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_auto_20151103_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='userId',
            new_name='user',
        ),
    ]
