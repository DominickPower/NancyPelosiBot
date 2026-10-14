from django.shortcuts import render
from django.http import HttpResponse
from . import API
from npb.models import Listing
import json
# Create your views here.

def populateDB(request):
    return API.databaseReader()

async def jsonStringReader(request):
    listings = list(Listing.objects.values("title", "category"))
    stringy = json.dumps(listings)
    return HttpResponse(stringy)