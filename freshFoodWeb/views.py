from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    page = 'home'
    return render (request, page + ".html")
