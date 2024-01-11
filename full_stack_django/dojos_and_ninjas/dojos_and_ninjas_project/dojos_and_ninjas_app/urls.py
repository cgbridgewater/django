from django.urls import path
from . import views
app_name = "dojos_and_ninjas_app"

urlpatterns = [
    path('', views.index, name="index"),
    path("create", views.create, name="create"),
    path("dojo/<int:id>/view", views.one_dojo, name="one_dojo"),
    path("dojo/<int:id>/delete", views.dojo_delete, name="dojo_delete"),
    path("ninja/<int:id>/view", views.one_ninja, name="one_ninja"),
    path("ninja/<int:id>/delete", views.ninja_delete, name="delete"),
]
