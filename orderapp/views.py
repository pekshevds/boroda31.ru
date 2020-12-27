from django.shortcuts import render
from django.shortcuts import redirect

from boroda31.core import get_context

from .core import get_order_by_id
from .core import put_cart_to_the_order
from .core import get_orders
from .core import set_order_is_sale

from .models import Order
from .models import OrderItem


from cartapp.core import get_cart

def show_order(request, id):
			
	context=get_context(request)
	context['order'] = get_order_by_id(id=id)
	return render(request, 'orderapp/order.html', context=context)

def create_order(request):
	
	cart = get_cart(request)['cart']
	customer = request.POST.get('customer', '')
	if customer == '' or cart.get_items_count == 0:
		return redirect(request.META['HTTP_REFERER'])
	
	return redirect('show_order', id=put_cart_to_the_order(cart, customer))

def show_orders(request):
	context=get_context(request)
	context['orders'] = get_orders(is_sale=False)
	return render(request, 'orderapp/orders.html', context=context)

def set_is_sale(request, id):
	order = get_order_by_id(id=id)
	if order:
		set_order_is_sale(order)

	return redirect('show_orders')
