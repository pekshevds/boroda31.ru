from django.contrib import admin
from .models import Order
from .models import OrderItem

# Register your models here.


class OrderItemInline(admin.TabularInline):

	model = OrderItem
	extra = 0

class OrderAdmin(admin.ModelAdmin):

	list_display = (		
		'customer',
		'id',
		'date',		
		'total',
		'is_sale',		
		'comment',
	)
	
	inlines = [OrderItemInline,]
	search_fields = ('id',)
	list_filter = ( 'is_sale', 'customer',)


admin.site.register(Order, OrderAdmin)