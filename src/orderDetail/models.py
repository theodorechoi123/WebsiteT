from django.db import models
from order.models import UserOrder

#Create your models here.
class OrderDetail(models.Model):
	orderDetailID = models.BigAutoField(primary_key=True)
	item = models.TextField()
	price = models.TextField()
	comment = models.TextField()
	orderID_ID = models.ForeignKey(UserOrder, on_delete=models.CASCADE, db_column='orderID')

	def __str__(self):
		return ''