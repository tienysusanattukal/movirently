from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def index(request):
    mov =Movie.objects.all()
    outcome = " , ". join ([m.name for m in mov])
    return HttpResponse(outcome)