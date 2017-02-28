# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0014_auto_20170228_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='food_item',
            new_name='Lanche',
        ),
    ]
