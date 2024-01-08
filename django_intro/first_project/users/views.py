from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return redirect("/users")

def users(request):
    return HttpResponse("placeholder to later display the list of all the users")


def register(request):
    return HttpResponse("placeholder for users to create a new user record")


def login(request):
    return HttpResponse("Placeholder for users to log in")


def new(request):
    if request.method == 'GET':
        return HttpResponse("placehoder to later create a new user feature")
    if request.method == 'POST':
        return redirect("/users")