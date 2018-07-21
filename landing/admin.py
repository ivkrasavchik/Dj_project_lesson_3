from django.contrib import admin
from .models import *

#  admin.site.register(Subscriber) # стандарт


# расширим отображение админки
class SubscriberAdmin(admin.ModelAdmin):
    #list_display = ["name", "email"]
    list_display = [field.name for field in Subscriber._meta.fields]  # выводит все поля
    list_filter = ['name',]  # выводит еще одно окно для назначения фильтра по указанному полю
    search_fields = ['name', 'email']  # выводит окно поиска действующее на указанные поля
    #exclude = ["email"]  # в окне редактирования исключает вывод указанных полей
    #inlines = []  # добавляет в поле встроенную форму (например в поле заказа, какие еще заказы вы уже сделали)
    fields = ['email']  # в окне редактирования выводятся только указанные поля
    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
