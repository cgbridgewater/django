from django.shortcuts import render, redirect
from .models import Dojo, Ninja


## index route ##
def index(request):
    context = {
        "all_dojos" : Dojo.objects.all()
    }
    return render(request, "dojos_and_ninjas_app/index.html", context)


## Create Route for dojos and ninjas ##
def create(request):
    if request.POST['posty_post'] == 'create_dojo':
        name = request.POST["name"]
        city = request.POST["city"]
        state = request.POST["state"]
        desc = request.POST["desc"]
        Dojo.objects.create(name=name, city=city, state=state, desc=desc)
        return redirect("/")
    elif request.POST['posty_post'] == 'create_ninja':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        dojo = Dojo.objects.get(id=request.POST["dojo"])
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
    return redirect("/")


## View One Dojo ##
def one_dojo(request, id):
    one_dojo = Dojo.objects.get(id=id)
    context = {
        "one_dojo" : one_dojo
    }
    return render(request, "dojos_and_ninjas_app/one_dojo.html", context)


## View One Ninja ##
def one_ninja(request, id):
    one_ninja = Ninja.objects.get(id=id)
    context = {
        "one_ninja" : one_ninja
    }
    return render(request, "dojos_and_ninjas_app/one_ninja.html", context)


## Delete Ninja Route ##
def ninja_delete(request, id):
    ninja_to_delete = Ninja.objects.get(id=id)
    ninja_to_delete.delete()
    return redirect("/")


## Delete Dojo Route ##
def dojo_delete(request, id):
    dojo_to_delete = Dojo.objects.get(id=id)
    dojo_to_delete.delete()
    return redirect("/")