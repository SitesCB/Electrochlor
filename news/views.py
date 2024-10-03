from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    categories = Category.objects.all()
    portfolio = Portfolio.objects.all()
    name = Name_Comp.objects.all()
    typeworks = TypeWork.objects.order_by('id')

    additional_serv = Additional_Services.objects.all()[::-1]

    prices = Price.objects.all()[::-1]

    context = {
        'typeworks' : typeworks,
        'name' : name[0].title,
        'cat' : categories,
        'por' : portfolio,
        'addit' : additional_serv,
        'prices' : prices,
    }
    return render(request, 'news/index.html', context)

def render_details(request, id):
    obj = Portfolio.objects.filter(id=id)
    name = Name_Comp.objects.all()
    print(obj[0].photo2)
    context = {
        'obj' : obj[0],
        'name' : name[0].title
    }

    return render(request, 'news/portfolio-details.html', context)

def thanks(req):

    return render(req, 'news/thanks.html', {})

def add_new(request):
    return render(request, 'news/add_new.html')

def get_category(request, category_id):
    print(category_id, 'id')
    news = News_Model.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news' : news,
        'categories' : categories,
        'category' : category,
    }
    return render(request, 'news/category.html', context)

def menu(request):

    photos = Photo.objects.all()
    photos1 = photos[:len(photos)//2 + 1]
    photos2 = photos[len(photos)//2::]

    context = {
        'photos1' : photos1,
        'photos2' : photos2,
    }

    return render(request, 'news/menu.html', context)


def generate_of_oxy(request):

    return render(request, 'news/Генерация окислителей.html')

def watering(request):
    return render(request, 'news/Дезинфекция воды.html')