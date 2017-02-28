# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0009_auto_20170228_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='table_number',
            field=models.DecimalField(default='0', max_digits=1, decimal_places=1),
        ),
    ]
