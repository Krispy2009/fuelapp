# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0008_auto_20150422_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=4)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('product_id', models.ForeignKey(to='prices.Product')),
                ('station_id', models.ForeignKey(to='prices.Station')),
            ],
            options={
                'verbose_name_plural': 'historical prices',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='station_id',
        ),
        migrations.DeleteModel(
            name='PriceHistory',
        ),
        migrations.AlterField(
            model_name='station',
            name='company',
            field=models.CharField(default=b'PL', max_length=32, choices=[(b'PL', b'Petrolina'), (b'EX', b'ExxonMobil'), (b'HP', b'Hellenic Petroleum'), (b'LO', b'Lukoil')]),
        ),
    ]
