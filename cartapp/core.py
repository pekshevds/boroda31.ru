from .models import Cart
from .models import CartItem


from catalogapp.models import Offer
from catalogapp.core import get_offer_by_slug


from decimal import Decimal


def add_to_cart(cart, offer, quant=1):

	items = CartItem.objects.filter(cart=cart, offer=offer)
	if items:

		item = items[0]
		item.quant = item.quant + quant
		item.save()
	else:
		items = CartItem.objects.create(cart=cart, offer=offer, quant=quant)	


def insert_to_cart(cart, offer, quant=1):

	CartItem.objects.filter(cart=cart, offer=offer).delete()	
	CartItem.objects.create(cart=cart, offer=offer, quant=quant)


def del_from_cart(cart, offer):
	
	try:
		CartItem.objects.filter(cart=cart, offer=offer).delete()
	except:
		pass	


def clear_cart(cart):
	
	try:
		CartItem.objects.filter(cart=cart).delete()
	except:
		pass	


def update_cart(request, cart):
	
	clear_cart(cart)

	counter = 1
	slug = request.POST.get("item"+str(counter), "")
	while slug != "":

		quant = request.POST.get("quant"+str(counter), 1) 

		add_to_cart(cart, get_offer_by_slug(slug), quant)

		counter = counter + 1
		slug = request.POST.get("item"+str(counter), "")


def get_cart_by_id(id):
	try:
		cart = Cart.objects.get(id=id)
	except:
		cart = Cart.objects.create()	

	return cart


def get_cart(request):
	cart = get_cart_by_id(request.session.get('cart_id'))	

	request.session['cart_id'] = cart.id
	return cart