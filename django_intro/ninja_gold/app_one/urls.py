from django.urls import path
from . import views

app_name = 'app_one'

urlpatterns = [
    path('', views.index, name="my_index"),
    path('process_money', views.process_money, name="process_money"),
    path('reset', views.reset, name="reset"),
]