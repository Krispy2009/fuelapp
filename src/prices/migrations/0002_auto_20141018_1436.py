# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(max_digits=5, decimal_places=4)),
                ('station_id', models.ForeignKey(to='prices.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='station_id',
        ),
        migrations.RemoveField(
            model_name='station',
            name='date',
        ),
        migrations.RemoveField(
            model_name='station',
            name='price',
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='product_id',
            field=models.ForeignKey(default=1, to='prices.Product'),
            preserve_default=False,
        ),
    ]
