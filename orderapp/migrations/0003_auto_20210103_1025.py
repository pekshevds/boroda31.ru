# Generated by Django 3.1.4 on 2021-01-03 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_auto_20201228_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_canceled',
            field=models.BooleanField(default=False, verbose_name='Отменен'),
        ),
        migrations.AddField(
            model_name='order',
            name='is_confirmed',
            field=models.BooleanField(default=False, verbose_name='Подтвержден'),
        ),
    ]