from django.shortcuts import render, redirect
import random
import datetime
now = datetime.datetime.now()
time = now.time().strftime("%I:%M %p")
date = now.date().strftime("%B-%d -%Y")

def index(request):
    # No activities or gold in session, make it! #
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "index.html")

# Standard way
# def process_money(request):
#     now = datetime.datetime.now()
#     time = now.time().strftime("%I:%M %p")
#     date = now.date().strftime("%B-%d -%Y")
#     if request.POST["gold_form"] == "farm":
#         winnings = random.randint(10, 20)
#         request.session['gold'] += winnings
#         request.session['activities'].insert(0,f"Earned {winnings} golds from the farm! ({time} - {date})")
#     elif request.POST["gold_form"] == "cave":
#         winnings = random.randint(5, 10)
#         request.session['gold'] += winnings
#         request.session['activities'].insert(0,f"Earned {winnings} golds from the cave! ({time} - {date})")
#     elif request.POST["gold_form"] == "house":
#         winnings = random.randint(2, 4)
#         request.session['gold'] += winnings
#         request.session['activities'].insert(0,f"Earned {winnings} golds from the house! ({time} - {date})")
#     elif request.POST["gold_form"] == "casino":
#         winnings = random.randint(-50, 50)
#         request.session['gold'] += winnings
#         if winnings > 0:
#             request.session['activities'].insert(0,f"Won {winnings} golds from the casino! ({time} - {date})")
#         elif winnings < 0:
#             request.session['activities'].insert(0,f"Lost {winnings} golds from the casino! ({time} - {date})")
#         else:
#             request.session['activities'].insert(0,f"No Gold Made at the Casino! ({time} - {date})")
#     elif request.POST["gold_form"] == "reset":
#         request.session['activities'] = []
#         request.session['gold'] = 0
#     return redirect("/")

def farm(request):
    winnings = random.randint(10, 20)
    request.session['gold'] += winnings
    request.session['activities'].insert(0,f"Earned {winnings} golds from the farm! ({time} - {date})")
    return redirect("/")

def cave(request):
    winnings = random.randint(5, 10)
    request.session['gold'] += winnings
    request.session['activities'].insert(0,f"Earned {winnings} golds from the cave! ({time} - {date})")
    return redirect("/")

def house(request):
    winnings = random.randint(2, 5)
    request.session['gold'] += winnings
    request.session['activities'].insert(0,f"Earned {winnings} golds from the house! ({time} - {date})")
    return redirect("/")

def casino(request):
    winnings = random.randint(-50, 50)
    request.session['gold'] += winnings
    if winnings > 0:
        request.session['activities'].insert(0,f"Won {winnings} golds from the casino! ({time} - {date})")
    elif winnings < 0:
        request.session['activities'].insert(0,f"Lost {winnings} golds from the casino! ({time} - {date})")
    else:
        request.session['activities'].insert(0,f"No Gold Made at the Casino! ({time} - {date})")
    return redirect("/")

def reset(request):
    request.session['activities'] = []
    request.session['gold'] = 0
    return redirect("/")