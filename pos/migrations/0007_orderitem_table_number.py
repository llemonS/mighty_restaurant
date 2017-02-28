# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_orderitem_client_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='table_number',
            field=models.DecimalField(default='0', max_digits=2, decimal_places=2),
        ),
    ]
