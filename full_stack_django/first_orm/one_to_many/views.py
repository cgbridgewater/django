from django.shortcuts import render
from .models import Book, Author

def index(request):
    context = {
        "all_authors" : Author.objects.all(),
        "dr_suess_books" : Author.objects.get(id=3).books.all()
    }

    return render(request, "one_to_many/index.html", context)
