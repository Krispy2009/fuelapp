# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0006_auto_20150215_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricehistory',
            name='slug',
            field=models.SlugField(default='slsls', unique=True),
            preserve_default=False,
        ),
    ]
