from .models import Order
from .models import OrderItem


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