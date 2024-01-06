from django.shortcuts import render
import random

def index(request):
    # initialize values #
    guesses = 0
    output = ''
    play_again = False
    game_over = False
    playing = False
    # if guesses not in session, create guesses session #
    if 'guesses' in request.session:
        guesses = request.session['guesses']
    # if magic number not in session, create magic number session #
    if 'num' in request.session:
        num = request.session['num']
    # create a random number for the magic number #
    else:
        num = random.randint(1, 100)
        request.session['num'] = num
    # console the magic number
    print(num)

    if request.method == 'POST':
        guesses += 1
        request.session['guesses'] = guesses
        playing = True
        guess = request.POST['guess']

        if int(guess) == num:
            request.session['score'] = guesses
            del request.session['guesses']
            del request.session['num']
            output = f'Winna Winna Chicken Dinna!  {num} was the number'
            play_again = True
            context = {
                'output': output,
                'play_again': play_again,
                'playing': playing,
                'game_over': game_over
            }
            return render(request, 'index.html', context)

        if int(guess) == 0:
            if guesses < 5:
                output = "No number entered! Turn Lost"
        elif int(guess) < num:
            output = 'Too Low'
        else:
            output = 'Too high'
        if guesses >= 5:
            del request.session['guesses']
            del request.session['num']
            game_over = True

    context = {
        'output': output,
        'play_again': play_again,
        'playing': playing,
        'game_over': game_over
    }
    return render(request, 'index.html', context)

# take second element for sort
def takeSecond(elem):
    return elem[1]

def scoreboard(request):
    print("name ", request.POST['name'])
    print("score ", request.session['score'])
    if not 'leaderboard' in request.session:
        request.session['leaderboard'] = []
    if request.method == 'POST':
        request.session['leaderboard'].append([request.POST['name'], request.session['score']])
        request.session['leaderboard'].sort(key= takeSecond )
        request.session['leaderboard']=request.session['leaderboard'][:10]
        request.session.save()
        request.session['current_score'] = request.POST['name'], request.session['score']
    return render(request, 'leaders.html')

