from django.db import models

#Create your models here.
class UserOrder(models.Model):
	orderID = models.BigAutoField(primary_key=True, default=0000)
	email = models.TextField()
	issuedDate = models.TextField()
	dueDate = models.TextField()
	isSameDay = models.BooleanField()
	isDelivery = models.BooleanField()
	isReady = models.BooleanField()

	def __str__(self):
		return ''