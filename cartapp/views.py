from django.shortcuts import render
from boroda31.core import get_context

from django.shortcuts import render
from django.shortcuts import redirect

from catalogapp.core import get_good_by_slug

from .core import get_cart
from .core import add_to_cart
from .core import insert_to_cart
from .core import del_from_cart
from .core import clear_cart

from decimal import Decimal

def show_cart(request):
	
	context = get_context(request)	
	return render(request, 'cartapp/cart.html', context)


def add_good_to_cart(request, slug):
	
	good = get_good_by_slug(slug=slug)
	quant = Decimal(request.POST.get('quant', 1))
	if good:

		cart = get_cart(request)
		add_to_cart(cart['cart'], good, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])


def insert_good_to_cart(request, slug):

	good = get_good_by_slug(slug=slug)
	quant = Decimal(request.POST.get('quant', 1))
	if good:

		cart = get_cart(request)
		insert_to_cart(cart['cart'], good, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])
	

def del_good_from_cart(request, slug):
	
	good = get_good_by_slug(slug=slug)
	if good:

		cart = get_cart(request)
		del_from_cart(cart['cart'], good)		

	return redirect(request.META['HTTP_REFERER'])

def clear_current_cart(request):
	
	cart = get_cart(request)
	clear_cart(cart['cart'])		

	return redirect(request.META['HTTP_REFERER'])


def plus_good_to_cart(request, slug):
	
	good = get_good_by_slug(slug=slug)
	quant = 1
	if good:

		cart = get_cart(request)
		add_to_cart(cart['cart'], good, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])

def minus_good_from_cart(request, slug):
	
	good = get_good_by_slug(slug=slug)
	quant = -1
	if good:

		cart = get_cart(request)
		add_to_cart(cart['cart'], good, quant=quant)		

	return redirect(request.META['HTTP_REFERER'])
