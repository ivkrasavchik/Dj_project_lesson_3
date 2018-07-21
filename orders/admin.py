from django.contrib import admin
from .models import *

#  admin.site.register(Subscriber) # стандарт
class ProductInOrderInLine(admin.TabularInline):
    model = ProductInOrder
    extra = 0

# расширим отображение админки
class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]  # выводит все поля

    class Meta:
        model = Status


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]  # выводит все поля
    inlines = [ProductInOrderInLine]
    class Meta:
        model = Order


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]  # выводит все поля

    class Meta:
        model = ProductInOrder


admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
