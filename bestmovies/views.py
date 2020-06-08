from django.shortcuts import render
from django.http import HttpResponse
from home.models import Movie

# Create your views here.


def English(request):
    movies = Movie.objects.filter(Movie_Language="English")
    context = {
        "movies": movies,
    }
    return render(request, 'English.html', context)


def Telugu(request):
    movies = Movie.objects.filter(Movie_Language="Telugu")
    context = {
        "movies": movies,
    }

    return render(request, 'Telugu.html', context)


def Home(request):
    return render(request,'Home.html')
