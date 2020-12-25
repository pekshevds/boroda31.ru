from .models import Cart
from .models import CartItem


from catalogapp.models import Good


from decimal import Decimal


def add_to_cart(cart, good, quant=1):

	items = CartItem.objects.filter(cart=cart, good=good)
	if items:

		item = items[0]
		item.quant = item.quant + quant
		item.save()
	else:
		items = CartItem.objects.create(cart=cart, good=good, quant=quant)	


def insert_to_cart(cart, good, quant=1):

	CartItem.objects.filter(cart=cart, good=good).delete()	
	CartItem.objects.create(cart=cart, good=good, quant=quant)


def del_from_cart(cart, good):
	
	try:
		CartItem.objects.filter(cart=cart, good=good).delete()
	except:
		return False
	return True


def clear_cart(cart):
	
	try:
		CartItem.objects.filter(cart=cart).delete()
	except:
		return False
	return True
	

def get_cartitems(cart):
	
	try:
		records = CartItem.objects.filter(cart=cart)
	except:
		records = None
	
	items = []
	if records:
		for item in records:
			
			good = item.good
			quant = item.quant

			items.append({
				'good'	: 	good,
				'quant'	: 	quant,
				'price'	: 	good.price,
				'sum'	: 	round(good.price * quant, 2),				
				})

	return items


def init_cart(cart):

	cart_sum = 0
	cart_quant = 0
	
	items = get_cartitems(cart)
	for item in items:
		cart_sum = cart_sum + item['sum']
		cart_quant = cart_quant + item['quant']
		

	return {
		'cart'		: cart,
		'cart_items': items,
		'cart_sum'	: cart_sum,
		'cart_quant': cart_quant,
	}


def get_cart_by_id(id):
	try:
		cart = Cart.objects.get(id=id)
	except:
		cart = Cart.objects.create()	

	return init_cart(cart)


def get_cart(request):
	cart = get_cart_by_id(request.session.get('cart_id'))	

	request.session['cart_id'] = cart['cart'].id
	return cart