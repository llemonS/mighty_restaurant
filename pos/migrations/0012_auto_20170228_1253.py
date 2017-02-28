# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0011_auto_20170228_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Nível_de_Acesso',
            new_name='access_level',
        ),
    ]
