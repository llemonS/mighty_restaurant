# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0010_auto_20170228_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='description',
            new_name='descrição',
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='price',
            new_name='preço',
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='access_level',
            new_name='Nível_de_Acesso',
        ),
    ]
