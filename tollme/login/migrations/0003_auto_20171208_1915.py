# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20171208_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='users',
            name='contact_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='vechile_no',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='vechile_type',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='vehicle_id',
            field=models.CharField(blank=True, db_column='vehicle_id', max_length=17, null=True),
        ),
    ]
