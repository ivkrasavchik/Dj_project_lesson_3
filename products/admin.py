from django.contrib import admin
from .models import *


#  admin.site.register(Subscriber) # стандарт
class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # выводит все поля
    inlines = [ProductImageInLine]
    class Meta:
        model = Product


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]  # выводит все поля

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)
