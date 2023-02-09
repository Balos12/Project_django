from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'merch/index.html')

def categories(request, catid):
    if int(catid) == 0:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Категорий товаров</h1><p1>{catid}</p1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

