# Generated by Django 5.0.4 on 2024-05-09 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='производитель')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=100, verbose_name='улица')),
                ('house', models.CharField(max_length=100, verbose_name='номер дома')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='производитель')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=100, verbose_name='улица')),
                ('house', models.CharField(max_length=100, verbose_name='номер дома')),
                ('type', models.CharField(choices=[('розничная сеть', 'розничная сеть'), ('предприниматель', 'предприниматель')], verbose_name='тип поставщика')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название товара')),
                ('model', models.CharField(max_length=100, verbose_name='модель товара')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='дата релиза')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producer', verbose_name='производитель')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=25, null=True, verbose_name='задолженность')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producer', verbose_name='производитель')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='продукт')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_supplier', to='products.supplier', verbose_name='поставщик')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_recipient', to='products.supplier', verbose_name='получатель')),
            ],
            options={
                'verbose_name': 'Поставка',
                'verbose_name_plural': 'Поставки',
            },
        ),
    ]
