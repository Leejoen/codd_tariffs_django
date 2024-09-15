from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    response = requests.get('https://static.maps.2gis.com/1.0?s=600x400@2x&c=55.7414,37.6209&zoom=13')
    return render(request, 'main/index.html')