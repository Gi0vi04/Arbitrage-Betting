import os
import requests

from utils.constants import BASE_URL, BOOKMAKERS

API_KEY = os.getenv('API_KEY')

def fetch_events(league):
    url = f"{BASE_URL}/{league}/events"
    params = {
        "apiKey": API_KEY,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()

def fetch_event_odds(league: str, event: str, market: str):
    url = f"{BASE_URL}/{league}/events/{event}/odds"
    params = {
        "apiKey": API_KEY,
        "regions": "eu",
        "markets": market,
        "bookmakers": ",".join(BOOKMAKERS)
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()