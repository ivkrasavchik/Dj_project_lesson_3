from django.shortcuts import render
from . forms import SubscriberForm
from products.models import *

def landing(request):
    name = "Haron"
    current_day = "19.07.2018"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():  # если форма отправляется методом post (как в html)
        #print(request.POST)
        #print(form.cleaned_data)  # для работы с полями формы используется только после form.is_valid()
        #data = form.cleaned_data
        #print(data[name])

        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__name="телефоны")
    products_images_laptops = products_images.filter(product__category__name="ноутбуки")
    return render(request, 'landing/home.html', locals())
