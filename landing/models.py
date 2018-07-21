from django.db import models


class Subscriber(models.Model):  # модели принято называть в ед. числе
    email = models.EmailField()
    name = models.CharField(max_length=128)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "My subscriber"  # приомзносимое имя в единственном числе
        verbose_name_plural = "A lot of subscribers"  # приомзносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "Пользователь  %s  %s" % (self.name, self.email)


