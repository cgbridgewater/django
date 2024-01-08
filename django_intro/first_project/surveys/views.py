from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
        return HttpResponse("placeholder to later display all the surveys created")

def new(request):
        return HttpResponse("place holder for users to add a new survey")