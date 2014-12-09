#-*- coding: utf8 -*-
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
#from django.contrib.auth.models import (
#	BaseUserManager, AbstractBaseUser)
from django.utils.html import format_html
import os  
# Create your models here.
class User(models.Model):
	user_id = models.CharField('User id',max_length=20,unique=True) #db_index=True
	password= models.CharField(max_length=20)
	idnum= models.AutoField('Id number',primary_key=True)
	name= models.CharField(max_length=20)#, unique=True db_index=True
	email= models.EmailField(blank =True)
	check_id=models.CharField(max_length=10 ,blank = True)

	def __unicode__(self):
		return str(self.idnum)

class Local(models.Model):
	local_id = models.IntegerField(primary_key=True)
	longitude= models.DecimalField(max_digits=12, decimal_places=8, default=0)
	latitude= models.DecimalField(max_digits=12, decimal_places=8, default=0)
	local_name= models.CharField('Location name', max_length=80)

	def __unicode__(self):
		return self.local_id
	
	class Meta(object):
		db_table ="local"

class Trip(models.Model):
	trip_id = models.IntegerField(primary_key=True)
	uid_id = models.ForeignKey('User',default=1)
	trip_name = models.CharField(max_length=100)
	trip_date = models.DateField(auto_now=False,auto_now_add=True)
	likes = models.IntegerField(default=0)
	counts= models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.trip_id


class Trip_Location(models.Model):
	no = models.IntegerField('Trip No.',primary_key=True)
	tid = models.ForeignKey('Trip')
	photo = models.FilePathField(path="/media",recursive=True,blank=True)
	lid = models.ForeignKey('Local')
	description = models.TextField(blank= True)
	dtime = models.DateTimeField('date published', auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.no

class Trip_Perform(models.Model):
	tripid = models.ForeignKey('Trip',primary_key=True)
	data = models.TextField(blank = True)
	modify_time =models.DateTimeField(auto_now=True,auto_now_add=True)
	permission = models.BooleanField()
	
	def __unicode__(self):
		return self.tripid

class Collect(models.Model):
	userid = models.ForeignKey('User',primary_key=True)
	ctrip = models.IntegerField()

	def __unicode__(self):
		return self.userid
