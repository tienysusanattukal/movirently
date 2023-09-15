from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def index(request):
    mov = Movie.objects.all()
    
    return render(request,'movies/index.html',{'movi':mov})