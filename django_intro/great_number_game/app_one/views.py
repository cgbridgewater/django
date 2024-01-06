from django.shortcuts import render
import random

def index(request):
    # initialize values #
    attempts = 0
    output = ''
    play_again = False
    game_over = False
    playing = False
    # if attempts not in session, create attempts session #
    if 'attempts' in request.session:
        attempts = request.session['attempts']
    # if magic number not in session, create magic number session #
    if 'number' in request.session:
        number = request.session['number']
    # create a random number for the magic number #
    else:
        number = random.randint(1, 100)
        request.session['number'] = number
    # console the magic number
    print(number)

    # If POST method increase attempts and compare numbers #
    if request.method == 'POST':
        attempts += 1
        request.session['attempts'] = attempts
        playing = True
        guess = request.POST['guess']
        
        # Winning Scenario #
        if int(guess) == number:
            request.session['score'] = attempts
            del request.session['attempts']
            del request.session['number']
            output = f'Winna Winna Chicken Dinna!  {number} was the number'
            play_again = True
            context = {
                'output': output,
                'play_again': play_again,
                'playing': playing,
                'game_over': game_over
            }
            return render(request, 'index.html', context)

        # No input Scenario #
        if int(guess) == 0:
            if attempts < 5:
                output = "No number entered! Turn Lost"
        # Low Guess Scenario #
        elif int(guess) < number:
            output = 'Too Low'
        # High Guess Scenario #
        else:
            output = 'Too high'
        
        # Straight Outta attempts Scenario #
        if attempts >= 5:
            del request.session['attempts']
            del request.session['number']
            game_over = True

    # context to send to page #
    context = {
        'output': output,
        'play_again': play_again,
        'playing': playing,
        'game_over': game_over
    }
    return render(request, 'index.html', context)

# take second element for sorting scoreboard #
def takeSecond(elem):
    return elem[1]

def scoreboard(request):
    # No Leaderboard in session, make it! #
    if not 'leaderboard' in request.session:
        request.session['leaderboard'] = []
    # If is a POST #
    if request.method == 'POST':
        # append score to leader board #
        request.session['leaderboard'].append([request.POST['name'], request.session['score']])
        # sort the leader board #
        request.session['leaderboard'].sort(key= takeSecond )
        # trim leader board to top 10 #
        request.session['leaderboard']=request.session['leaderboard'][:10]
        # save it to session #
        request.session.save()
        # create a current score to post #
        request.session['current_score'] = request.POST['name'], request.session['score']
    return render(request, 'leaders.html')