from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def index(request):
    mov = Movie.objects.all()
    
    return render(request,'index.html',{'movi':mov})