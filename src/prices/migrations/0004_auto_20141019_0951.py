# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_auto_20141019_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 19, 9, 51, 31, 249753), auto_now_add=True),
            preserve_default=False,
        ),
    ]
