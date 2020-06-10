
from django.db import models


class Movie(models.Model):
    Image = models.ImageField(upload_to='photos/')
    Image2 = models.ImageField(upload_to='photos/', default='DEFAULT VALUE')
    Image3 = models.ImageField(upload_to='photos/', default='DEFAULT VALUE')
    Image4 = models.ImageField(upload_to='photos/', default='DEFAULT VALUE')

    Movie_title = models.CharField(max_length=50)
    Director = models.CharField(max_length=40)
    Starring = models.CharField(max_length=130)
    Production_company = models.CharField(max_length=100)
    Release_Date = models.CharField(max_length=15)
    Movie_Language = models.CharField(max_length=20, default='DEFAULT VALUE')
    Synopsis = models.CharField(max_length=400,default='DEFAULT VALUE')
    year = models.CharField(max_length=20, default='DEFAULT VALUE')
    Genre = models.CharField(max_length=20,default='DEFAULT VALUE')
    link = models.CharField(max_length=60,default='DEFAULT VALUE')
    def __str__(self):
        return self.Movie_title
