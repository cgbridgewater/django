from django.urls import path
from . import views
app_name = "dojos_and_ninjas_app"

urlpatterns = [
    path('', views.index, name="index"),
    path("create", views.create, name="create"),
    path("ninja/<int:id>/delete", views.delete, name="delete"),
    path("dojo/<int:id>/view", views.one_dojo, name="one_dojo"),
    path("ninja/<int:id>/view", views.one_ninja, name="one_ninja"),
]
