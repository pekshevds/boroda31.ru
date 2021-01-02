# Generated by Django 3.1.4 on 2020-12-30 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0012_auto_20201227_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Наименование')),
                ('slug', models.SlugField(blank=True, max_length=300, verbose_name='Url')),
                ('is_show', models.BooleanField(default=False, verbose_name='Виден для пользователей')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogapp.menuitem', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]