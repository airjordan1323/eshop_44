# Generated by Django 4.2.6 on 2023-10-18 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название продукта')),
                ('description', models.TextField(verbose_name='Описание продукта')),
                ('price', models.FloatField(verbose_name='Цена продукта')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Количество товара')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Категория продукта')),
            ],
        ),
    ]
