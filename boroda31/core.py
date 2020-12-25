from catalogapp.core import get_categoryes

def get_context(request):
	
	return {
		'categoryes': get_categoryes(),
	}