# Generated by Django 3.1.4 on 2020-12-26 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogapp', '0005_auto_20201225_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='set_additive', to='catalogapp.good', verbose_name='Добавка')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='set_good', to='catalogapp.good', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Набор',
                'verbose_name_plural': 'Наборы',
            },
        ),
    ]
