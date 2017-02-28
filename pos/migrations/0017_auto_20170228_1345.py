# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0016_auto_20170228_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='notes',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='dados',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
