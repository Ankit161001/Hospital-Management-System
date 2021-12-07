from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.TextField()
	description = models.TextField()
	spec = models.TextField()