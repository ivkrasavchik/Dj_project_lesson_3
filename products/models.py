from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64)
    is_activ = models.BooleanField(default=True)
    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Категория товара"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Категория товаров"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.name


class Product(models.Model):  # модели принято называть в ед. числе
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=50, blank=True, null=True, default=None)
    description = models.TextField(max_length=256, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Товар"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Товары"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s %s" % (self.price, self.name)


class ProductImage(models.Model):  # модели принято называть в ед. числе
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Фото"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Фотографии"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.id
