# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0017_auto_20170228_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='access_level',
            new_name='nível_de_acesso',
        ),
    ]
