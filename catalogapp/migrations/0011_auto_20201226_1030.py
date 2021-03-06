# Generated by Django 3.1.4 on 2020-12-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0010_auto_20201226_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='slug',
            field=models.SlugField(blank=True, max_length=1600, unique=True, verbose_name='Url'),
        ),
        migrations.AlterUniqueTogether(
            name='offer',
            unique_together=set(),
        ),
    ]
