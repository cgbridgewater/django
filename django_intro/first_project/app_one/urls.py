from django.urls import path
from . import views
app_name = "blogs"

urlpatterns = [
    path('', views.index, name="index"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('<int:id>', views.show, name="show"),
    path('<int:id>/edit', views.edit, name="edit"),
    path('<int:id>/delete', views.destroy, name="destroy"),
    path('json', views.bonus, name="bonus",)
]

