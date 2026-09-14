import requests
import json
from django.http import HttpResponse
from npb.models import Listing
url = "https://external-api.kalshi.com/trade-api/v2/events?status=open"
response = requests.get(url)
open_events_json = response.json()
events = open_events_json["events"]

def createKalshiListing(ticker):
    url = f"https://external-api.kalshi.com/trade-api/v2/events/{ticker}"
    eventResponse = requests.get(eventURL)
    dict = eventResponse["event"].json()
    newListing = Listing(title = dict["title"], category = dict["category"])
    
    print(newListing.title)
    
def kalshiSerializer():
    return HttpResponse(response.status_code)