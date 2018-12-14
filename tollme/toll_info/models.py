# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login.models import Users
# Create your models here.


class Orders(models.Model):
    orderid = models.CharField(db_column='OrderId', max_length=100)  # Field name made lowercase.
    fdate = models.DateField(blank=True, null=True)
    amount = models.CharField(db_column='Amount', max_length=20)  # Field name made lowercase.
    tollid = models.IntegerField(db_column='TollId')  # Field name made lowercase.
    route = models.CharField(db_column='Route', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50)  # Field name made lowercase.
    user = models.ForeignKey(Users,db_column='User_Id', unique=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=1000, blank=True, null=True)  # Field name made lowercase.



    class Meta:
        managed = False
        db_table = 'Orders'



class Places(models.Model):
    place_id = models.AutoField(db_column='Place_Id', primary_key=True)  # Field name made lowercase.
    place_name = models.CharField(db_column='Place_Name', max_length=200)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude')  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Places'


class Routedetails(models.Model):
    routeid = models.AutoField(db_column='RouteId', primary_key=True)  # Field name made lowercase.
    fpid = models.IntegerField(db_column='FPId')  # Field name made lowercase.
    tpid = models.IntegerField(db_column='TPId')  # Field name made lowercase.
    rname = models.CharField(db_column='RName', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RouteDetails'


class Tolldetails(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude')  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude')  # Field name made lowercase.
    tollname = models.CharField(db_column='TollName', max_length=1000)  # Field name made lowercase.
    tollplazaid = models.IntegerField(db_column='TollPlazaId')  # Field name made lowercase.
    carrate_single = models.IntegerField(db_column='CarRate_single')  # Field name made lowercase.
    fourtosixexel_single = models.IntegerField(db_column='FourToSixExel_Single')  # Field name made lowercase.
    busrate_multi = models.IntegerField(db_column='BusRate_multi')  # Field name made lowercase.
    lcvrate_single = models.IntegerField(db_column='LCVRate_single')  # Field name made lowercase.
    multiaxlerate_single = models.IntegerField(db_column='MultiAxleRate_single')  # Field name made lowercase.
    sevenormoreexel_single = models.IntegerField(db_column='SevenOrmoreExel_Single')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TollDetails'


class Tolltaxes(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    rid = models.IntegerField(db_column='RId')  # Field name made lowercase.
    tollid = models.IntegerField(db_column='TollId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TollTaxes'


class Tolls(models.Model):
    tollid = models.AutoField(db_column='TollId', primary_key=True)  # Field name made lowercase.
    tollname = models.CharField(db_column='TollName', max_length=500)  # Field name made lowercase.
    tolltax = models.IntegerField(db_column='TollTax')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tolls'
