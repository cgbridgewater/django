from django.shortcuts import render
from time import localtime, strftime
import datetime

    
def index(request):
    context = {
        "time": strftime("%I:%M %p", localtime()),
        "date": strftime("%B-%d -%Y", localtime())
    }
    return render(request,'index.html', context)

def alt_time(request):
    now = datetime.datetime.now()
    context = {
        "time": now.time().strftime("%I:%M %p"),
        "date": now.date().strftime("%B-%d -%Y")
    }
    return render(request,'alt.html', context)