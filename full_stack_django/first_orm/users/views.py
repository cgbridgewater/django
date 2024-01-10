from django.shortcuts import render
from .models import Users

# Create your views here.

def index(request):
    context = {
        "all_users" : Users.objects.all()
    }
    return render(request, "users/index.html", context)
