# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toll_info', '0004_auto_20171209_0620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]