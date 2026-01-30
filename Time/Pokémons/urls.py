from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('time', views.time, name = 'time'),
    path('time/lugia', views.lugia, name = 'lugia'),
    path('time/charizard', views.charizard, name = 'charizard'),
    path('time/rayquaza', views.rayquaza, name = 'rayquaza'),
    path('time/torterra', views.charizard, name = 'torterra'),
    path('time/suicune', views.rayquaza, name = 'suicune'),
    path('time/mimikyu', views.mimikyu, name = 'mimikyu'),
]