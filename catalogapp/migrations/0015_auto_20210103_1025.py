# Generated by Django 3.1.4 on 2021-01-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0014_category_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='weight',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=15, verbose_name='Вес, гр'),
        ),
    ]
