import requests

url = "https://external-api.kalshi.com/trade-api/v2/events?status=open"
response = requests.get(url)
open_events_json = response.json()
events = open_events_json["events"]
print(events)
