# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricehistory',
            name='station_id',
            field=models.ForeignKey(default=1, to='prices.Station'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pricehistory',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='station',
            name='city',
            field=models.CharField(default=b'NIC', max_length=16, choices=[(b'NIC', b'Nicosia'), (b'LAR', b'Larnaca'), (b'LIM', b'Limassol'), (b'PAF', b'Paphos'), (b'FAM', b'Famagusta')]),
        ),
    ]
