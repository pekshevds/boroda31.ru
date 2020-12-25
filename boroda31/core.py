from catalogapp.core import get_categoryes
from cartapp.core import get_cart

def get_context(request):
	
	return {
		'categoryes': get_categoryes(),
		'cart': get_cart(request),
	}