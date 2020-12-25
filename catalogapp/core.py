from .models import Category
from .models import Good

import random

def get_categoryes():

	return Category.objects.all()
	

def get_category_by_slug(slug):
	
	return Category.objects.get(slug=slug)


def get_good_by_slug(slug):
    
    return Good.objects.get(slug=slug)


def get_category_goods(category):
    try:
        goods = Good.objects.filter(category=category)
    except:
        return None

    if goods:        
        return goods
    return None


def get_recommendations():
    
    goods = Good.objects.all()
    
    if len(goods) > 5:
        
        recommendations = set()
        while len(recommendations) < 4:

            number = random.randint(0, len(goods)-2)
            recommendations.add(goods[number])

        return list(recommendations)
    return None
