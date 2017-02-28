# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0007_orderitem_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='table_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
