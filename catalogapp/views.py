from django.shortcuts import render

def show_list(request):
		
	return render(request, 'catalogapp/list.html', context={})