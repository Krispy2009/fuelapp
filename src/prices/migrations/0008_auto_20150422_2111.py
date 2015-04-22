# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0007_pricehistory_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='station_id',
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='slug',
            field=models.SlugField(unique=True, editable=False),
        ),
    ]
