from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('increase', views.increase),
    path('decrease', views.decrease),
    path('logout', views.delete)
]