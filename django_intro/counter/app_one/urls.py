from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('increase', views.increase),
    path('decrease', views.decrease),
    path('modify', views.modify),
    path('destroy_session', views.delete)
]