from django.urls import path
from . import views

app_name = "one_to_many"

urlpatterns = [
    path('', views.index, name="index"),
]
