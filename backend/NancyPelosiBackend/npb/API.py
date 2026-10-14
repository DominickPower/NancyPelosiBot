import requests
import json
from django.http import HttpResponse
from .models import Listing
import uuid

#Licence: Dominick Richard Power 09-10-2026
#This class contains all data transfer API functions for this app
class DataAPI:
    VALID_SITES = {"kalshi": 'https://external-api.kalshi.com/trade-api/v2/events', "polymarket": "https://gamma-api.polymarket.com/events/keyset"}
    def __init__(self, key):
        self.key = key
    
    #Populate: Populates the database with results from a given site so long as the site is in our list of approved sites
    #Parameters:
    #   target: Target site for the population. Must be contained in the global VALID_SITES list
    #   cursorDepth: How many pages we want to go through. Default to 1
    #   pageLimit: Limits the amount of results per page. Default to 50
    #   staus: Defines which status we want. Defaults to "open"
    #Creates a certain amount of Listing objects based on Page limit and Cursor Depth, Then pushes them all to the database
    def populate(self, target, cursorDepth=1, pageLimit = 50, status="open"):
        match target.lower():
            case "kalshi":
                #Because we dont always want to add a cursor, we don't use the starter as a hard coded string
                CURSOR_STARTER = "?cursor="
                url = self.VALID_SITES["kalshi"] + f"?limit=" + pageLimit + "?status=" + status
                objList = []
                resp = requests.get(url)
                raw = resp.json()
                event_list = raw["events"]

                if (cursorDepth == 1):
                    objList = objList + self._getListingsFromPage(event_list)
                else:
                    for i in range(cursorDepth):            
                        cursor = raw["cursor"]
                        objList = objList + self._getListingsFromPage(event_list)
                        nextPage = url + CURSOR_STARTER + cursor
                        raw = HttpResponse.get(nextPage)
                        #Get the new event list before repeating the loop again
                        event_list = raw["events"]

                Listing.objects.bulk_create(objList)

    def databaseReader():
        listingData = Listing.objects.all()
        listingData2 = listingData.filter(category="world")
        print(listingData2)
        return(HttpResponse("200"))

    def _getListingsFromPage(self, event_list):
        pageList = []
        for event in event_list:
            dbObject = Listing(title = event["title"], ticker = event["event_ticker"], LastUpdated = event["last_updated_ts"], category = event["category"])
            pageList.append(dbObject)
        return pageList