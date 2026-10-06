import requests
import json
from django.http import HttpResponse
from ..models import Listing
import uuid

url = "https://external-api.kalshi.com/trade-api/v2/events?status=open"
response = requests.get(url)
open_events_json = response.json()
events = open_events_json["events"]


#PSEUDOCODE FOR PARSING EVENT DATA
# Get all events
# iterate through all events
# Create the corresponding model object from those events
# add each object to a list
# once we have iterated through all events, push each object to the database at once

def populate(cursorDepth=0):
    url = f"https://external-api.kalshi.com/trade-api/v2/events/"
    eventResponse = requests.get(url)
    jsonData = eventResponse.json()
    rawEventList = jsonData['events']
    parsedEventList = []
    for event in rawEventList:
        #Data we want is Title, EventTicker, LastUpdated, and Category
        event = Listing(title=event["title"], ticker=event["event_ticker"], LastUpdated=event["last_updated_ts"], category=event["category"])
        parsedEventList.append(event)
    Listing.objects.bulk_create(parsedEventList)
    return(HttpResponse("200"))

def databaseReader():
    listingData = Listing.objects.all()
    listingData2 = listingData.filter(category="world")
    print(listingData2)
    return(HttpResponse("200"))
