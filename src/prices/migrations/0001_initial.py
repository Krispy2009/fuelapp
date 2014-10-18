# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(max_digits=5, decimal_places=4)),
                ('company', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='station_id',
            field=models.ForeignKey(to='prices.Station'),
            preserve_default=True,
        ),
    ]
