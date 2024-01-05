from django.shortcuts import render, HttpResponse, redirect


def index(request):
    request.session['count'] = 0
    return render(request, "index.html")


def create(request):
    print("Got Post Info...............")
    request.session['name'] = request.POST['name']
    # count = 0
    # count += int(request.POST['counter'])
    # request.session['count'] = count
    request.session['count'] += int(request.POST['counter'])
    print("count", request.session['count'])
    print("name", request.session['name'])

    context = {

    }
    return render(request, "results.html", context)


def increase(request):
    request.session['count'] += 1
    return render(request, "results.html")

def decrease(request):
    request.session['count'] -= 1
    return render(request, "results.html")


def delete(request):
    del request.session['name'] 
    del request.session['count']
    return redirect("/")