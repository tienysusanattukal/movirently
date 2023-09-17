from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movie
# Create your views here.
def index(request):
    mov = Movie.objects.all()
    
    return render(request,'movies/index.html',{'movi':mov})

def detail(request,movie_id):
    
    mo = get_object_or_404(Movie, pk=movie_id)
    return render(request,'movies/detail.html',{'moo':mo})


