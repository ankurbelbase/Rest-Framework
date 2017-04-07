from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):

	name = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	date = models.DateField()

	# to print object in admin.py
	def __str__(self):
		return self.name

		#to represent two different app (eg. to web to phone)
	def __repr__(self):
		return self.name

