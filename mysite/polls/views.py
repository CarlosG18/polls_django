from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World, you'are at the polls index")

# Create your views here.
