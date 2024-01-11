from django.urls import path, include

urlpatterns = [
    path('', include("dojos_and_ninjas_app.urls"), name= "dojos_and_ninjas_app"),
]
