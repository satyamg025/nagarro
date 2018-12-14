# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(db_column='OrderId', max_length=100)),
                ('tollid', models.IntegerField(db_column='TollId')),
                ('route', models.CharField(blank=True, db_column='Route', max_length=1000, null=True)),
                ('status', models.CharField(db_column='Status', max_length=50)),
                ('amount', models.CharField(db_column='Amount', max_length=20)),
                ('fdate', models.DateField(blank=True, null=True)),
                ('type', models.IntegerField(db_column='Type')),
                ('filename', models.CharField(db_column='FileName', max_length=500)),
            ],
            options={
                'db_table': 'Orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('place_id', models.AutoField(db_column='Place_Id', primary_key=True, serialize=False)),
                ('place_name', models.CharField(db_column='Place_Name', max_length=200)),
                ('latitude', models.FloatField(db_column='Latitude')),
                ('longitude', models.FloatField(db_column='Longitude')),
            ],
            options={
                'db_table': 'Places',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Routedetails',
            fields=[
                ('routeid', models.AutoField(db_column='RouteId', primary_key=True, serialize=False)),
                ('fpid', models.IntegerField(db_column='FPId')),
                ('tpid', models.IntegerField(db_column='TPId')),
                ('rname', models.CharField(db_column='RName', max_length=1000)),
            ],
            options={
                'db_table': 'RouteDetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tolldetails',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('latitude', models.FloatField(db_column='Latitude')),
                ('longitude', models.FloatField(db_column='Longitude')),
                ('tollname', models.CharField(db_column='TollName', max_length=1000)),
                ('tollplazaid', models.IntegerField(db_column='TollPlazaId')),
                ('carrate_single', models.IntegerField(db_column='CarRate_single')),
                ('fourtosixexel_single', models.IntegerField(db_column='FourToSixExel_Single')),
                ('busrate_multi', models.IntegerField(db_column='BusRate_multi')),
                ('lcvrate_single', models.IntegerField(db_column='LCVRate_single')),
                ('multiaxlerate_single', models.IntegerField(db_column='MultiAxleRate_single')),
                ('sevenormoreexel_single', models.IntegerField(db_column='SevenOrmoreExel_Single')),
            ],
            options={
                'db_table': 'TollDetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tolls',
            fields=[
                ('tollid', models.AutoField(db_column='TollId', primary_key=True, serialize=False)),
                ('tollname', models.CharField(db_column='TollName', max_length=500)),
                ('tolltax', models.IntegerField(db_column='TollTax')),
            ],
            options={
                'db_table': 'Tolls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tolltaxes',
            fields=[
                ('sno', models.AutoField(db_column='Sno', primary_key=True, serialize=False)),
                ('rid', models.IntegerField(db_column='RId')),
                ('tollid', models.IntegerField(db_column='TollId')),
            ],
            options={
                'db_table': 'TollTaxes',
                'managed': False,
            },
        ),
    ]
