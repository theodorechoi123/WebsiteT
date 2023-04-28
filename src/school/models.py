from django.db import models

# Create your models here.

PRIORITY = [
	("H", "High"),
	("M", "Medium"),
	("L", "Low"),
]

class Question(models.Model):
	# We put 5 tabs for organization purposes
	title					= models.CharField(max_length = 60)
	question				= models.TextField(max_length = 400)
	priority				= models.CharField(max_length = 1, choices = PRIORITY)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Questions"
		verbose_name_plural = "Peoples Questions"