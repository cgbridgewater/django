from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse


def root(request):
    return redirect("/blogs")


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/")



def show(request, id):
    return HttpResponse(f"placeholder to display a blog number: {id}")


def edit(request, id):
    return HttpResponse(f"placeholder to edit blog number: {id}")


def destroy(request, id):
    return redirect("/blogs")


def bonus(request):
    return JsonResponse({
        "title":"My first blog",
        " content": "Lorem, ipsum dolor sit amet consectuter adipisicing elit."
    })