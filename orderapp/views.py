from django.shortcuts import render

def show_order(request):
		
	return render(request, 'orderapp/order.html', context={})