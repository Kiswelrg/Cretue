from django.db import models

# Create your models here.
class Record(models.Model):
	class Meta:
		"""docstring for Metaf __init__(self, arg):
			super(Meta__init__()
			self.arg = arg
		"""
		unique_together = (('index', 'id'), )

	index = models.AutoField(primary_key=True, unique=True)
	id = models.CharField(max_length=20, unique=True)
	keymode = models.IntegerField(null=True)
	ssmode = models.IntegerField(null=True)
	transc = models.IntegerField(null=True)
	lesson = models.IntegerField(null=True)
	grades = models.IntegerField(null=True)
	selected = models.IntegerField(null=True)
	friend = models.IntegerField(null=True)
	dateCreated = models.DateTimeField()
	error = models.IntegerField(null=True)

class Stuxh(models.Model):
	id = models.CharField(max_length=12, unique=True, primary_key=True)
	name = models.CharField(max_length=12)
	institute = models.CharField(max_length=20, null=True)
	major = models.CharField(max_length=20, null=True)

class Count(models.Model):
	num = models.IntegerField()

class offList(models.Model):
	lessonid = models.CharField(max_length=12, unique=True, primary_key=True)

class offList6(models.Model):
	lessonid = models.CharField(max_length=12, unique=True, primary_key=True)