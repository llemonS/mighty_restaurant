# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0004_auto_20161023_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_level',
            field=models.CharField(max_length=1, choices=[('s', 'Garçom'), ('c', 'Cozinheiro'), ('o', 'Registrador')]),
        ),
    ]
