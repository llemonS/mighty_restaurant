# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0015_auto_20170228_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Lanche',
            new_name='lanches',
        ),
    ]
