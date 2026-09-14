from django.shortcuts import render
from django.http import HttpResponse
from .ApiCalls import kalshi
# Create your views here.

def populateDB(request):
    return kalshi.kalshiSerializer()