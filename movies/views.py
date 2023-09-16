from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Movie
# Create your views here.
def index(request):
    mov = Movie.objects.all()
    
    return render(request,'movies/index.html',{'movi':mov})

def detail(request,movie_id):
    try:
        mo = Movie.objects.get(pk=movie_id)
        return render(request,'movies/detail.html',{'moo':mo})
    except Movie.DoesNotExist:
        raise Http404()

