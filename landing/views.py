from django.shortcuts import render
from . forms import SubscriberForm

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

