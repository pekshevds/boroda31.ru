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
        goods = Good.objects.filter(category=category, is_show=True)
    except:
        return None

    if goods:        
        return goods
    return None


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
    
    if len(goods) > 4:
        
        recommendations = set()
        while len(recommendations) < 4:

            number = random.randint(0, len(goods)-2)
            recommendations.add(goods[number])

        return list(recommendations)
    return None
