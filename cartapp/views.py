from django.shortcuts import render
from boroda31.core import get_context

from django.shortcuts import render
from django.shortcuts import redirect

from catalogapp.core import get_good_by_slug
from catalogapp.core import find_good_by_slug
from catalogapp.core import get_offer_by_slug
from catalogapp.core import get_offer_by_key_fields

from .core import get_cart
from .core import add_to_cart
from .core import insert_to_cart
from .core import del_from_cart
from .core import clear_cart
from .core import update_cart

from decimal import Decimal

def show_cart(request):
	
	context = get_context(request)	
	return render(request, 'cartapp/cart.html', context)


def add_good_to_cart(request, slug):
	
	good = get_good_by_slug(slug=slug)
	
	additive1 = find_good_by_slug(slug=request.POST.get('additive1', ""))
	additive2 = find_good_by_slug(slug=request.POST.get('additive2', ""))
	additive3 = find_good_by_slug(slug=request.POST.get('additive3', ""))
	additive4 = find_good_by_slug(slug=request.POST.get('additive4', ""))
	additive5 = find_good_by_slug(slug=request.POST.get('additive5', ""))

	quant1 = int(request.POST.get('quant1', '0'))
	quant2 = int(request.POST.get('quant2', '0'))
	quant3 = int(request.POST.get('quant3', '0'))
	quant4 = int(request.POST.get('quant4', '0'))
	quant5 = int(request.POST.get('quant5', '0'))

	quant = int(request.POST.get('quant', '1'))
	if good:

		offer = get_offer_by_key_fields(good, additive1, additive2, additive3, additive4, additive5, quant1, quant2, quant3, quant4, quant5)
		cart = get_cart(request)
		add_to_cart(cart['cart'], offer, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])


def insert_good_to_cart(request, slug):

	good = get_good_by_slug(slug=slug)
	
	additive1 = find_good_by_slug(slug=request.POST.get('additive1', ""))
	additive2 = find_good_by_slug(slug=request.POST.get('additive2', ""))
	additive3 = find_good_by_slug(slug=request.POST.get('additive3', ""))
	additive4 = find_good_by_slug(slug=request.POST.get('additive4', ""))
	additive5 = find_good_by_slug(slug=request.POST.get('additive5', ""))

	quant1 = int(request.POST.get('quant1', '0'))
	quant2 = int(request.POST.get('quant2', '0'))
	quant3 = int(request.POST.get('quant3', '0'))
	quant4 = int(request.POST.get('quant4', '0'))
	quant5 = int(request.POST.get('quant5', '0'))

	quant = int(request.POST.get('quant', '1'))
	if good:

		offer = get_offer_by_key_fields(good, additive1, additive2, additive3, additive4, additive5, quant1, quant2, quant3, quant4, quant5)
		cart = get_cart(request)
		insert_to_cart(cart['cart'], offer, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])
	

def del_good_from_cart(request, slug):
	
	offer = get_offer_by_slug(slug=slug)
	if offer:

		cart = get_cart(request)
		del_from_cart(cart['cart'], offer)		

	return redirect(request.META['HTTP_REFERER'])


def clear_current_cart(request):
	
	cart = get_cart(request)
	clear_cart(cart['cart'])		

	return redirect(request.META['HTTP_REFERER'])


def update_current_cart(request):
	
	cart = get_cart(request)
	update_cart(request, cart['cart'])		

	return redirect(request.META['HTTP_REFERER'])


def plus_good_to_cart(request, slug):
	
	offer = get_offer_by_slug(slug=slug)
	quant = 1
	if offer:

		cart = get_cart(request)
		add_to_cart(cart['cart'], offer, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])

def minus_good_from_cart(request, slug):
	
	offer = get_offer_by_slug(slug=slug)
	quant = -1
	if offer:

		cart = get_cart(request)
		add_to_cart(cart['cart'], offer, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])
