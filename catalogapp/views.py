from django.shortcuts import render

from boroda31.core import get_context

from .core import get_menu_by_slug
from .core import get_good_by_slug
from .core import get_recommendations
from .core import get_good_additive


def show_list(request, slug):
		
	context=get_context(request)
	context['menu'] = get_menu_by_slug(slug)
	# context['items'] = get_category_goods(context['category'])


	return render(request, 'catalogapp/list.html', context)


def show_item(request, slug):
		
	context=get_context(request)	
	context['item'] = get_good_by_slug(slug)
	context['recommendations'] = get_recommendations()
	context['additives'] = get_good_additive(context['item'])	

	return render(request, 'catalogapp/item.html', context)