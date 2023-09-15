from django.contrib import admin
from .models import Genre,Movie
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display =('id','name')

class MovieAdmin(admin.ModelAdmin):
    list_display =('id','name','year_of_release','genre','no_of_dvd_for_rent','rental_rate_per_day')

admin.site.register(Genre,GenreAdmin)
admin.site.register(Movie,MovieAdmin)