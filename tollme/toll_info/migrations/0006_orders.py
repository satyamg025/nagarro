# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 06:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20171209_0556'),
        ('toll_info', '0005_delete_orders'),
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
                ('user', models.ForeignKey(db_column='User_Id', on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
    ]
