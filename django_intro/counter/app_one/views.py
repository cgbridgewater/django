from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    # else:


    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1

    return render(request, "index.html")

def increase(request):
    request.session['count'] += 2
    request.session['visits'] -= 1
    return redirect('/')

def decrease(request):
    request.session['count'] -= 2
    request.session['visits'] -= 1
    return redirect('/')

def modify(request):
    print("Got Post Info...............")
    request.session['count'] = int(request.POST['counter'])
    request.session['visits'] -= 1
    return redirect('/')

def delete(request):
    request.session['count'] = 0
    request.session['visits'] = 0
    return redirect("/")