from django.db import models


from django.template.defaultfilters import slugify
from unidecode import unidecode
# Create your models here.
import uuid

def get_uuid4():
    return str(uuid.uuid4())


def get_uuid():
    return str(uuid.uuid4().fields[0])


def get_image_name(instance, filename):
    new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.slug
    return new_name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)    
    picture = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 200х200', default=None, null=True, blank=True)
    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)

    is_show = models.BooleanField(verbose_name="Виден для пользователей", default=False)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        
        try:
            self.slug = slugify(unidecode(self.name))  
        except:
            pass

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Good(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    site_name = models.CharField(max_length=255, verbose_name="Наименование для магазина", null=True, blank=True)
    art = models.CharField(max_length=25, verbose_name="Артикул", null=True, blank=True, default='')        
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    slug = models.SlugField(max_length=300, verbose_name='Url', blank=True, db_index=True)

    is_sale = models.BooleanField(verbose_name="Распродажа", default=False)
    is_new = models.BooleanField(verbose_name="Новинка", default=False)
    is_hot = models.BooleanField(verbose_name="Спецпредложение", default=False)
    is_service = models.BooleanField(verbose_name="Услуга", default=False)
    is_show = models.BooleanField(verbose_name="Доступен в меню", default=False)

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT, blank=True, null=True)

    price = models.DecimalField(verbose_name='Цена', default=0, max_digits=15, decimal_places=2, blank=True)
    old_price = models.DecimalField(verbose_name='Старая цена', default=0, max_digits=15, decimal_places=2, blank=True)
    discount = models.DecimalField(verbose_name='Скидка, %', default=0, max_digits=15, decimal_places=2, blank=True)

    quant = models.DecimalField(verbose_name='Количество', default=0, max_digits=15, decimal_places=0)

    width = models.DecimalField(verbose_name='Ширина, см', default=0, max_digits=15, decimal_places=1)
    height = models.DecimalField(verbose_name='Высота, см', default=0, max_digits=15, decimal_places=1)
    depth = models.DecimalField(verbose_name='Глубина, см', default=0, max_digits=15, decimal_places=1)
    weight = models.DecimalField(verbose_name='Вес, кг', default=0, max_digits=15, decimal_places=3)
    volume = models.DecimalField(verbose_name='Объем, м3', default=0, max_digits=15, decimal_places=5)

    additive1 = models.ForeignKey('self', verbose_name="Добавка 1", related_name="good_additive1", on_delete=models.PROTECT, blank=True, null=True)
    additive2 = models.ForeignKey('self', verbose_name="Добавка 2", related_name="good_additive2", on_delete=models.PROTECT, blank=True, null=True)
    additive3 = models.ForeignKey('self', verbose_name="Добавка 3", related_name="good_additive3", on_delete=models.PROTECT, blank=True, null=True)
    additive4 = models.ForeignKey('self', verbose_name="Добавка 4", related_name="good_additive4", on_delete=models.PROTECT, blank=True, null=True)
    additive5 = models.ForeignKey('self', verbose_name="Добавка 5", related_name="good_additive5", on_delete=models.PROTECT, blank=True, null=True)
    

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):


        if not self.site_name:
            self.site_name = self.name        

        try:
            self.slug = slugify(unidecode(self.site_name))  
        except:
            pass

        volume = self.width/10 * self.height/10 * self.depth/10
        if self.volume == 0:
            self.volume = volume

        super(Good, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'


def add_name(name, additive, postfix=""):
    if additive:
        if name != "":
            name = name + "; " + (additive.name + "-" + postfix)
        else:
            name = name + (additive.name + "-" + postfix)

    return name


def add_slug(slug, additive, postfix=""):
    if additive:
        if slug != "":
            slug = slug + "-" + (additive.slug + "_" + postfix)
        else:
            slug = slug + (additive.slug + "_" + postfix)

    return slug


class Offer(models.Model):
    slug = models.SlugField(max_length=1600, verbose_name='Url', blank=True, db_index=True, unique=True)

    good = models.ForeignKey(Good, verbose_name='Номенклатура', related_name="offer_good", on_delete=models.PROTECT)

    additive1 = models.ForeignKey(Good, verbose_name="Добавка 1", related_name="offer_additive1", on_delete=models.PROTECT, blank=True, null=True)
    quant1 = models.DecimalField(verbose_name='Количество 1', default=0, max_digits=15, decimal_places=0, blank=True)
    additive2 = models.ForeignKey(Good, verbose_name="Добавка 2", related_name="offer_additive2", on_delete=models.PROTECT, blank=True, null=True)
    quant2 = models.DecimalField(verbose_name='Количество 2', default=0, max_digits=15, decimal_places=0, blank=True)
    additive3 = models.ForeignKey(Good, verbose_name="Добавка 3", related_name="offer_additive3", on_delete=models.PROTECT, blank=True, null=True)
    quant3 = models.DecimalField(verbose_name='Количество 3', default=0, max_digits=15, decimal_places=0, blank=True)
    additive4 = models.ForeignKey(Good, verbose_name="Добавка 4", related_name="offer_additive4", on_delete=models.PROTECT, blank=True, null=True)
    quant4 = models.DecimalField(verbose_name='Количество 4', default=0, max_digits=15, decimal_places=0, blank=True)
    additive5 = models.ForeignKey(Good, verbose_name="Добавка 5", related_name="offer_additive5", on_delete=models.PROTECT, blank=True, null=True)
    quant5 = models.DecimalField(verbose_name='Количество 5', default=0, max_digits=15, decimal_places=0, blank=True)


    def __str__(self):
        
        name = ""

        if self.quant1 > 0:
            name = add_name(name, self.additive1, str(self.quant1))
        if self.quant2 > 0:
            name = add_name(name, self.additive2, str(self.quant2))
        if self.quant3 > 0:
            name = add_name(name, self.additive3, str(self.quant3))
        if self.quant4 > 0:
            name = add_name(name, self.additive4, str(self.quant4))
        if self.quant5 > 0:
            name = add_name(name, self.additive5, str(self.quant5))  
        
        return "Добавки: " + name


    def save(self, *args, **kwargs):
            
        slug = ""

        slug = add_slug(slug, self.good, str(1))
        slug = add_slug(slug, self.additive1, str(self.quant1))
        slug = add_slug(slug, self.additive2, str(self.quant2))
        slug = add_slug(slug, self.additive3, str(self.quant3))
        slug = add_slug(slug, self.additive4, str(self.quant4))
        slug = add_slug(slug, self.additive5, str(self.quant5))
        
        self.slug = slug
        super(Offer, self).save(*args, **kwargs)


    def get_sum(self):
        sum = self.good.price

        if self.additive1:
            sum = sum + (self.additive1.price * self.quant1)

        if self.additive2:
            sum = sum + (self.additive2.price * self.quant2)

        if self.additive3:
            sum = sum + (self.additive3.price * self.quant3)

        if self.additive4:
            sum = sum + (self.additive4.price * self.quant4)

        if self.additive5:
            sum = sum + (self.additive5.price * self.quant5)

        return sum


    class Meta:

        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'


class Picture(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', blank=True)
    slug = models.SlugField(max_length=36, verbose_name='Url', blank=True, db_index=True)
    good = models.ForeignKey('Good', verbose_name='Номенклатура', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 500x500', default=None, null=True, blank=True)
    is_main = models.BooleanField(verbose_name='Основная картинка', default=False)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = get_uuid()
            self.title = self.slug

        super(Picture, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'