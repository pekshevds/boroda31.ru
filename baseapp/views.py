from django.shortcuts import render
from boroda31.core import get_context
from orderapp.core import get_most_popular
from catalogapp.core import get_is_sale
from catalogapp.core import get_is_new
from catalogapp.core import get_is_hot

def show_index(request):
		
	context = get_context(request)
	context['most_popular'] = get_most_popular()
	context['is_sale'] = get_is_sale()
	context['is_new'] = get_is_new()
	context['is_hot'] = get_is_hot()
	return render(request, 'baseapp/index.html', context=context)


def show_contacts(request):
	context = get_context(request)
	
	return render(request, 'baseapp/contacts.html', context=context)