
from django.db import models


class Movie(models.Model):
    Movie_title = models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    Starring = models.CharField(max_length=200)
    Production_company = models.CharField(max_length=200)
    Release_Date = models.CharField(max_length=15)
    Movie_Language = models.CharField(max_length=20, default='DEFAULT VALUE')
    
    def __str__(self):
        return self.Movie_title
