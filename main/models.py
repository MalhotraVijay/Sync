from django.db import models


# Create your models here.

class myAccount(models.Model):
	labName = models.CharField(max_length=30)
	adminUsername = models.CharField(max_length=40)
	adminPassword = models.CharField(max_length=40)
	adminEmail = models.CharField(max_length=40)

	class Meta:
		db_table = 'myAccount'


class subLabs(models.Model):
	labName = models.CharField(max_length=30)
	labType = models.CharField(max_length=40)
	labLocation = models.CharField(max_length=40)
	labEmail = models.CharField(max_length=40)
	labContact = models.CharField(max_length=13)			
	adminUsername = models.CharField(max_length=20)
	adminPassword = models.CharField(max_length=20)
	class Meta:
		db_table = 'subLabs'



class uploadFiles(models.Model):
	upFiles = models.FileField(upload_to= 'myfiles/')
	upBranch = models.CharField(max_length = 30)

	class Meta:
		db_table = 'uploadFiles'



