from django.db import models
from catalogapp.models import Offer

from decimal import Decimal


# Create your models here.
class Order(models.Model):	
	customer = models.CharField(max_length=25, verbose_name="Заказчик", null=False, blank=False)
	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)	
	total = models.DecimalField(verbose_name="Сумма заказа", default=0, max_digits=15, decimal_places=2, blank=True)
	сook_by = models.DateTimeField(verbose_name="Приготовить к", auto_now_add=True)
	comment = models.CharField(max_length=1024, verbose_name="Комментарий", default='', null=True, blank=True)

	weight = models.DecimalField(verbose_name='Вес, кг', default=0, max_digits=15, decimal_places=3, blank=True)
	volume = models.DecimalField(verbose_name='Объем, м3', default=0, max_digits=15, decimal_places=5, blank=True)

	is_sale = models.BooleanField(verbose_name="Подтвержден", default=False)

	def __str__(self):
		return str(self.id) + ' от ' + self.date.strftime("%d.%m.%Y")

	def save(self, *args, **kwargs):
		
		
		self.total = 0
		items = OrderItem.objects.filter(order=self)
		
		result = items.aggregate(models.Sum('total'))		
		if result['total__sum']:
			self.total = result['total__sum']

		result = items.aggregate(models.Sum('weight'))		
		if result['weight__sum']:
			self.weight = result['weight__sum']

		result = items.aggregate(models.Sum('volume'))		
		if result['volume__sum']:
			self.volume = result['volume__sum']

		super(Order, self).save(*args, **kwargs)


	def get_order_items(self):
		items = OrderItem.objects.filter(order=self)
		if items:
			return items
		return None		


	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'	


class OrderItem(models.Model):
	order = models.ForeignKey(Order, verbose_name="Корзина", on_delete=models.CASCADE)
	offer = models.ForeignKey(Offer, verbose_name="Предложение", on_delete=models.PROTECT, null=True,)
	quant = models.DecimalField(verbose_name='Количество', default=1, max_digits=15, decimal_places=0)
	price = models.DecimalField(verbose_name='Цена', default=0, max_digits=15, decimal_places=2)
	discount = models.DecimalField(verbose_name='Скидка, %', default=0, max_digits=15, decimal_places=2)
	total = models.DecimalField(verbose_name='Сумма', default=0, max_digits=15, decimal_places=2)

	weight = models.DecimalField(verbose_name='Вес, кг', default=0, max_digits=15, decimal_places=3)
	volume = models.DecimalField(verbose_name='Объем, м3', default=0, max_digits=15, decimal_places=5)

	def save(self, *args, **kwargs):
				
		self.total = self.price * Decimal(self.quant)
		self.weight = self.offer.good.weight * Decimal(self.quant)
		self.volume = self.offer.good.volume * Decimal(self.quant)

		super(OrderItem, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Строка заказа'
		verbose_name_plural = 'Строки заказа'