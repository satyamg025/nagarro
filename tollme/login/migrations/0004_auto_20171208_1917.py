# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 19:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20171208_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='vechile_type',
            new_name='vehicle_type',
        ),
    ]
