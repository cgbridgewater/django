from django.urls import path, include

urlpatterns = [
    path('', include('users.urls'), name="users"),
    path('blogs/', include('app_one.urls'), name="blogs"),
    path('surveys/', include('surveys.urls'), name="surveys"),
]
