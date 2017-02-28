# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0013_auto_20170228_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='table_number',
        ),
        migrations.AddField(
            model_name='ticket',
            name='client_name',
            field=models.CharField(max_length=255, default=''),
        ),
        migrations.AddField(
            model_name='ticket',
            name='table_number',
            field=models.DecimalField(default='0', max_digits=1, decimal_places=1),
        ),
    ]
