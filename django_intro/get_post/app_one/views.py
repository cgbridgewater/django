from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def create_user(request):
    print("Got Post Info...............")
    name_from_form = request.POST["name"]
    email_from_form = request.POST["email"]
    text_from_form = request.POST["text"]
    ninja_from_form = request.POST["ninja"]
    if 'spam' not in request.POST:
        spam_from_form = "No Thanks"
    else:
        spam_from_form = request.POST['spam']
    print("ninja", ninja_from_form)
    print("spam", spam_from_form)
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form,
        "text_on_template" : text_from_form,
        "ninja_on_template" : ninja_from_form,
        "spam_on_template" : spam_from_form
    }
    return render(request, "results.html", context)