from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('time', views.time, name = 'time'),
    path('time/lugia', views.lugia, name = 'lugia'),
    path('time/charizard', views.charizard, name = 'charizard'),
    path('time/rayquaza', views.rayquaza, name = 'rayquaza'),
    path('time/torterra', views.torterra, name = 'torterra'),
    path('time/suicune', views.suicune, name = 'suicune'),
    path('time/mimikyu', views.mimikyu, name = 'mimikyu'),
    path('time/charizard/mega', views.mega_charizard, name = 'charizardmega'),
    path('time/rayquaza/mega', views.mega_rayquaza, name = 'rayquazamega')
]