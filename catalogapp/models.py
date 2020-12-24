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
    is_show = models.BooleanField(verbose_name="Виден для пользователей", default=False)

    category = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.PROTECT, blank=True, null=True)

    price = models.DecimalField(verbose_name='Цена', default=0, max_digits=15, decimal_places=2)
    quant = models.DecimalField(verbose_name='Количество', default=0, max_digits=15, decimal_places=3)

    width = models.DecimalField(verbose_name='Ширина, см', default=0, max_digits=15, decimal_places=1)
    height = models.DecimalField(verbose_name='Высота, см', default=0, max_digits=15, decimal_places=1)
    depth = models.DecimalField(verbose_name='Глубина, см', default=0, max_digits=15, decimal_places=1)
    weight = models.DecimalField(verbose_name='Вес, кг', default=0, max_digits=15, decimal_places=3)
    volume = models.DecimalField(verbose_name='Объем, м3', default=0, max_digits=15, decimal_places=5)


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