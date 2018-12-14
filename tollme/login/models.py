# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Users(models.Model):
    user_name = models.CharField(max_length=500, blank=True, null=True)
    vehicle_no = models.CharField(unique=True, max_length=17, blank=True, null=True)
    vehicle_type = models.CharField(max_length=500, blank=True, null=True)
    users_address = models.CharField(max_length=500, blank=True, null=True)
    contact_no = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'
