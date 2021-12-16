from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.TextField()
	description = models.TextField()
	spec = models.TextField()
	image = models.ImageField(blank = True, null = True)

class Ambulance(models.Model):
	name = models.TextField()
	number = models.TextField()