from django.shortcuts import render
from boroda31.core import get_context

def show_index(request):
		
	return render(request, 'baseapp/index.html', context=get_context(request))
