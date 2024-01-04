from django.urls import path
from . import views	

urlpatterns = [
    path('', views.index),
    path('alttime', views.alt_time),
]