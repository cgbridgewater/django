from django.shortcuts import render, redirect
import random
import datetime
now = datetime.datetime.now()
time = now.time().strftime("%I:%M %p")
date = now.date().strftime("%B-%d -%Y")

def index(request):
    # No activities or gold in session, make it! #
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, "index.html")


def process_money(request):
    # Farm Action #
    if request.POST["gold_form"] == "farm":
        winnings = random.randint(10, 20)
        result = (f"Earned {winnings} golds from the farm! ({time} - {date})")
    # Cave Action #
    elif request.POST["gold_form"] == "cave":
        winnings = random.randint(5, 10)
        result = (f"Earned {winnings} golds from the cave! ({time} - {date})")
    # House Action #
    elif request.POST["gold_form"] == "house":
        winnings = random.randint(2, 4)
        result = (f"Earned {winnings} golds from the house! ({time} - {date})")
    # Casino Action #
    elif request.POST["gold_form"] == "casino":
        winnings = random.randint(-50, 50)
        if winnings > 0:
            result = (f"Won {winnings} golds from the casino! ({time} - {date})")
        elif winnings < 0:
            result = (f"Lost {winnings} golds from the casino! ({time} - {date})")
        else:
            result = (f"No Gold Made at the Casino! ({time} - {date})")
    # process route into sessions #
    request.session['gold'] += winnings
    request.session['activities'].insert(0, result)
    request.session.save()

    return redirect("/")

# reset page #
def reset(request):
    request.session['activities'] = []
    request.session['gold'] = 0

    return redirect("/")