from django.db import models
from products.models import Product
from django.db.models import signals

class Status(models.Model):  # модели принято называть в ед. числе
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Статус заказа"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Статусы заказа"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "Статус  %s" % self.name


class Order(models.Model):  # модели принято называть в ед. числе
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # total price for all products in order
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(max_length=256, blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Заказ"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Заказы"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "Заказ  %s %s" % (self.id, self.status.name)


class ProductInOrder(models.Model):  # модели принято называть в ед. числе
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Товар в заказе"  # приомзносимое имя в единственном числе
        verbose_name_plural = "Товары в заказе"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.product.name

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.nmb * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order

    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


signals.post_save.connect(product_in_order_post_save, sender=ProductInOrder)
