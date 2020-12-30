from .models import Order
from .models import OrderItem

from catalogapp.models import Offer

from django.db.models import Avg, Max, Min, Count, Sum



def get_order_by_id(id):
	try:
		order = Order.objects.get(id=id)
	except:
		order = None
	return order


def get_orders(is_sale=True):
	return Order.objects.filter(is_sale=is_sale)
	

def set_order_is_sale(order):
	
	order.is_sale = True
	order.save()	


def put_cart_to_the_order(cart, customer, comment=''):
	
	order = Order.objects.create(customer=customer, comment=comment)

	cart_items = cart.get_cart_items()
	for cart_item in cart_items:
		order_item = OrderItem.objects.create(order=order, 
											offer=cart_item.offer, 
											quant=cart_item.quant, 
											price=cart_item.offer.good.price)

	order.save()
	cart.clear_cart()
	return order.id


def get_most_popular():

	try:
		records = OrderItem.objects.values('offer').annotate(quant=Sum('quant')).order_by('quant')
	except:
		records = None
	
	most_popular = set()
	if records:
		for item in records:
			
			offer = Offer.objects.get(id=item['offer'])
			if offer.good.is_show:
				most_popular.add(offer.good)

	return list(most_popular)[:4]
