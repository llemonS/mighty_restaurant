# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_auto_20161023_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
