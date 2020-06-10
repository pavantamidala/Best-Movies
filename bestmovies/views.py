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


def Animation(request):
    movies = Movie.objects.filter(Movie_Language="Animation")
    context = {
        "movies": movies,
    }

    return render(request, 'Animation.html', context)


def Malayalam(request):
    movies = Movie.objects.filter(Movie_Language="Malayalam")
    context = {
        "movies": movies,
    }

    return render(request, 'Malayalam.html', context)


def Hindi(request):
    movies = Movie.objects.filter(Movie_Language="Hindi")
    context = {
        "movies": movies,
    }

    return render(request, 'Hindi.html', context)


def Korean(request):
    movies = Movie.objects.filter(Movie_Language="Korean")
    context = {
        "movies": movies,
    }

    return render(request, 'Korean.html', context)


def Horror(request):
    movies = Movie.objects.filter(Movie_Language="Horror")
    context = {
        "movies": movies,
    }

    return render(request, 'Horror.html', context)


def Action(request):
    movies = Movie.objects.filter(Movie_Language="Action")
    context = {
        "movies": movies,
    }

    return render(request, 'Action.html', context)
