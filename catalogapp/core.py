from .models import Category
from .models import Good
from .models import Offer
from .models import Picture
from .models import MenuItem

import random


def get_main_menu():

    return MenuItem.objects.filter(parent=None, is_show=True)


def get_menu_by_slug(slug):
    
    return MenuItem.objects.get(slug=slug)


def get_menu_categoryes(menu):

    return Category.objects.filter(menu=menu, is_show=True)


def get_categoryes():

	return Category.objects.filter(is_show=True)
	

def get_category_by_slug(slug):
	
	return Category.objects.get(slug=slug)


def get_good_by_slug(slug):
    
    return Good.objects.get(slug=slug)


def find_good_by_slug(slug):
    
    goods = Good.objects.filter(slug=slug)
    if goods:
        return goods[0]
    return None


def get_offer_by_slug(slug):
    
    return Offer.objects.get(slug=slug)


def find_offer_by_slug(slug):
    
    offers = Offer.objects.filter(slug=slug)
    if offers:
        return offers[0]
    return None


def get_offer_by_key_fields(good, 
                            additive1, additive2, additive3, additive4, additive5,
                            quant1, quant2, quant3, quant4, quant5):
    try:
        
        offer = Offer.objects.get(good=good, 
                            additive1=additive1, additive2=additive2, additive3=additive3, additive4=additive4, additive5=additive5,
                            quant1=quant1, quant2=quant2, quant3=quant3, quant4=quant4, quant5=quant5)
    except:
        offer = None

    if not offer:
        offer = Offer.objects.create(good=good, 
                            additive1=additive1, additive2=additive2, additive3=additive3, additive4=additive4, additive5=additive5,
                            quant1=quant1, quant2=quant2, quant3=quant3, quant4=quant4, quant5=quant5)

    return offer


def get_good_additive(good):
    additives = set()

    if good.additive1:
        additives.add(good.additive1)

    if good.additive2:
        additives.add(good.additive2)

    if good.additive3:
        additives.add(good.additive3)

    if good.additive4:
        additives.add(good.additive4)

    if good.additive5:
        additives.add(good.additive5)

    return additives


def get_recommendations():    
    goods = Good.objects.filter(is_show=True)
    if goods:
        if len(goods) > 4:
        
            recommendations = set()
            while len(recommendations) < 4:

                number = random.randint(0, len(goods)-2)
                recommendations.add(goods[number])

            return list(recommendations)
    return None


def get_is_sale():
    goods = Good.objects.filter(is_show=True, is_sale=True)
    
    return goods
    

def get_is_new():
    goods = Good.objects.filter(is_show=True, is_new=True)
    
    return goods

def get_is_hot():
    goods = Good.objects.filter(is_show=True, is_hot=True)
    
    return goods