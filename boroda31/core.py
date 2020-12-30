from catalogapp.core import get_main_menu
from cartapp.core import get_cart

def get_context(request):
	
	return {
		'mainmenu': get_main_menu(),
		'cart': get_cart(request),
	}



