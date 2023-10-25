from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Название категории",
                            max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(verbose_name="Название продукта", max_length=256)
    description = models.TextField(verbose_name="Описание продукта")
    category = models.ForeignKey(verbose_name="Категория продукта", to=Category, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name="Цена продукта")
    amount = models.PositiveSmallIntegerField(verbose_name="Количество товара")
    photo = models.ImageField(verbose_name="Картинка", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Cart(models.Model):
    user_id = models.PositiveIntegerField(verbose_name="ID пользователя")
    product_id = models.ForeignKey(verbose_name="Продукт", to=Products, on_delete=models.PROTECT)
    count = models.PositiveSmallIntegerField(verbose_name="Количество товаров для покупки", default=1)

    def __str__(self):
        return f"{self.product_id} - {self.user_id}"

    class Meta:
        verbose_name = "Корзину"
        verbose_name_plural = "Корзина"
