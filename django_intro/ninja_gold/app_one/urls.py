from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('process_money', views.process_money), #standard way
    path('process_money/farm', views.farm),
    path('process_money/cave', views.cave),
    path('process_money/house', views.house),
    path('process_money/casino', views.casino),
    path('process_money/reset', views.reset),
]