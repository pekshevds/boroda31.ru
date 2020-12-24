from django.shortcuts import render

def show_wishlist(request):
		
	return render(request, 'wishlistapp/wishlist.html', context={})