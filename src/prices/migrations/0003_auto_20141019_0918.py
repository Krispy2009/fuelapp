# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20141018_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='unleaded-98', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='station',
            name='slug',
            field=models.SlugField(default='agios-dometios-high-street', unique=True),
            preserve_default=False,
        ),
    ]
