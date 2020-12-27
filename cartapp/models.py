from django.db import models
from catalogapp.models import Offer

from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
	user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT, null=True, blank=True)
	
	def get_cart_items(self):
		items = CartItem.objects.filter(order=self)
		if items:
			return items
		return None


	def get_cart_items(self):
		items = CartItem.objects.filter(cart=self)
		if items:
			return items
		return None


	def get_items_count(self):
		items = get_cart_items(self)
		if items:
			return len(items)
		return 0


	def clear_cart(self):	
		try:
			CartItem.objects.filter(cart=self).delete()
		except:
			pass


	class Meta:
		verbose_name = 'Корзина'
		verbose_name_plural = 'Корзина'	


class CartItem(models.Model):
	cart = models.ForeignKey(Cart, verbose_name="Корзина", on_delete=models.CASCADE)
	offer = models.ForeignKey(Offer, verbose_name="Предложение", on_delete=models.PROTECT, null=True,)
	quant = models.DecimalField(verbose_name='Количество', default=1, max_digits=15, decimal_places=0)
    
	def __str__(self):
		return self.offer.good.name

	class Meta:
		verbose_name = 'Элементы корзины'
		verbose_name_plural = 'Элемент корзины'