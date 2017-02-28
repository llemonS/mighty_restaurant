# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0012_auto_20170228_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='descrição',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='preço',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='titulo',
            new_name='title',
        ),
    ]
