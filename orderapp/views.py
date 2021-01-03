from django.shortcuts import render
from django.shortcuts import redirect


from boroda31.core import get_context

from .core import get_order_by_id
from .core import put_cart_to_the_order
from .core import get_orders
from .core import set_order_is_confirmed
from .core import set_order_is_canceled


from .models import Order
from .models import OrderItem


from cartapp.core import get_cart


def show_order(request, id):
			
	context=get_context(request)
	context['order'] = get_order_by_id(id=id)
	return render(request, 'orderapp/order.html', context=context)


def create_order(request):
	
	cart = get_cart(request)
	customer = request.POST.get('customer', '')
	comment = request.POST.get('comment', '')
	if customer == '' or cart.get_items_count == 0:
		return redirect(request.META['HTTP_REFERER'])
	
	return redirect('show_order', id=put_cart_to_the_order(cart, customer, comment))


def show_orders(request):
	context=get_context(request)
	context['orders'] = get_orders()
	context['title'] = 'Заказы в работе'
	return render(request, 'orderapp/orders.html', context=context)


def show_canceled(request):
	context=get_context(request)
	context['orders'] = get_orders(is_canceled=True)
	context['title'] = 'Отмененые'
	return render(request, 'orderapp/orders.html', context=context)


def show_confirmed(request):
	context=get_context(request)
	context['orders'] = get_orders(is_confirmed=True)
	context['title'] = 'Подтвержденные'
	return render(request, 'orderapp/orders.html', context=context)


def set_is_confirmed(request, id):
	order = get_order_by_id(id=id)
	if order:
		set_order_is_confirmed(order)

	return redirect('show_orders')


def set_is_canceled(request, id):
	order = get_order_by_id(id=id)
	if order:
		set_order_is_canceled(order)

	return redirect('show_orders')
