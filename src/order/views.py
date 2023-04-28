from django.shortcuts import render
from .models import UserOrder
from account.models import Account
from django.db import connection


def OrderView(request):
	context = {}
	currentUserEmail = request.user.email
	context['order'] = UserOrder.objects.raw("SELECT * FROM order_userorder WHERE email = %s", [currentUserEmail])

	return render(request, 'order/order.html', context)


