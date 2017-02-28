# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0005_auto_20170228_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='client_name',
            field=models.CharField(max_length=255, default=''),
        ),
    ]
