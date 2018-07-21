from django.db import models



class Product(models.Model):  # модели принято называть в ед. числе
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
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
    image = models.ImageField(upload_to='product_images')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Фото"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Фотографии"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.id
