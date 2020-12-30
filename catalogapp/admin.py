from django.contrib import admin

from .models import Good
from .models import Category
from .models import Picture
from .models import Offer
from .models import MenuItem
# Register your models here.

class PictureInline(admin.TabularInline):
    model = Picture
    exclude = ('title', 'slug')
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'menu',
    )

    list_filter = ( 'menu',)

    search_fields = ('name',)


class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'good',
        'slug',

    )

    search_fields = ('name',)


class GoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'site_name',
        'category',        
        'is_sale',
        'is_new',
        'is_hot',
        'is_service',
        'is_show',
        'price',
    )

    inlines = [PictureInline, ]

    list_filter = ( 'category', 'is_sale', 'is_new', 'is_hot', 'is_service', 'is_show',)

    search_fields = ('name',)

    readonly_fields = ('slug', )    


class MenuItemAdmin(admin.ModelAdmin):

    list_display = (        
        'name',
        'parent',       
    )   


admin.site.register(Category, CategoryAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(MenuItem, MenuItemAdmin)