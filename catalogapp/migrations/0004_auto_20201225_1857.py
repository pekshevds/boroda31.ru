# Generated by Django 3.0.5 on 2020-12-25 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0003_auto_20201225_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='Скидка, %'),
        ),
        migrations.AlterField(
            model_name='good',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='Старая цена'),
        ),
        migrations.AlterField(
            model_name='good',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, verbose_name='Цена'),
        ),
    ]
