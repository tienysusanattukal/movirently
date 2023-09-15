from django.db import models
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey('Genre',on_delete=models.CASCADE)
    year_of_release = models.IntegerField()
    no_of_dvd_for_rent = models.IntegerField()
    rental_rate_per_day = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)

    