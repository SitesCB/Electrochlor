from django.urls import path
from .views import *
# точка указывает на текущую директорию

urlpatterns = [
    path('', index),
    path('menu', menu),
    path('Генерация окислителей', generate_of_oxy),
    path('Дезинфекция воды', watering)
]


