from django.shortcuts import render
from .models import OrderDetail
from order.models import UserOrder
from django.db import connection

# Create your views here.
def OrderDetailView(request, orderID):
    context = {}
    orderDetail = OrderDetail.objects.filter(orderID_ID=orderID)
    context['orderDetail'] = orderDetail
    print(f'order_id: {orderID}')
    #context['orderDetail'] = OrderDetail.objects.raw("SELECT * FROM orderDetail_orderdetail od JOIN order_userorder o ON od.orderID = o.orderID WHERE orderID = %s", [id])
    return render(request, 'orderDetail/orderDetail.html', context)