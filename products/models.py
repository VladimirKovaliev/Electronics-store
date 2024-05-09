from django.db import models

from users.models import NULLABLE


class Producer(models.Model):
    """Модель производителя"""

    title = models.CharField(max_length=100, unique=True, verbose_name='производитель')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house = models.CharField(max_length=100, verbose_name='номер дома')

    def __str__(self):
        return f'Товар: {self.title}, email: {self.email}'

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Product(models.Model):
    """Модель товара"""

    title = models.CharField(max_length=100, verbose_name='название товара')
    model = models.CharField(max_length=100, verbose_name='модель товара')
    release_date = models.DateField(auto_now_add=True, verbose_name='дата релиза')
    provider = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='производитель')

    def __str__(self):
        return f'Товар: {self.title}, модель: {self.model}, производитель: {self.provider}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Supplier(models.Model):
    """Модель поставщика"""

    DISTRIBUTOR = 'розничная сеть'
    ENTREPRENEUR = 'предприниматель'

    supplier_type = (
        (DISTRIBUTOR, 'розничная сеть'),
        (ENTREPRENEUR, 'предприниматель')
    )

    title = models.CharField(max_length=100, unique=True, verbose_name='производитель')
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house = models.CharField(max_length=100, verbose_name='номер дома')
    type = models.CharField(choices=supplier_type, verbose_name='тип поставщика')

    def __str__(self):
        return f'Производитель: {self.title}, Тип поставщика: {self.type}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Supply(models.Model):
    """Модель поставки"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='производитель')
    provider = models.ForeignKey(Supplier, related_name='related_supplier', on_delete=models.CASCADE,
                                 verbose_name='поставщик', **NULLABLE)
    recipient = models.ForeignKey(Supplier, related_name='related_recipient', on_delete=models.CASCADE,
                                  verbose_name='получатель', **NULLABLE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    debt = models.DecimalField(decimal_places=2, max_digits=25, verbose_name='задолженность', **NULLABLE)

    def __str__(self):
        return f'Продукт: {self.product}, производитель: {self.producer}'

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
