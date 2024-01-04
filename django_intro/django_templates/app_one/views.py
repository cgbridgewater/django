from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "name": "Chris",
        "favorite_color": "Orange",
        "pets": ["Nibbler", "Yogi Bear", "Juniper"]
    }
    return render(request, "index.html", context)

def show(request, name):
    context = {"name": name}
    return render(request,"helloname.html", context)