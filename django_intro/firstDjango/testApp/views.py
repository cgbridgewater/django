from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def one_method(request):
    pass

def another_method(request, my_val):
    pass

def yet_another(request, name):
    pass

def one_more(request, id, color):
    pass

def root_method(request):
    return HttpResponse("String response from root_method")
def another_method(request):
    return redirect("/redirected_route")
def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})