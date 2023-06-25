import requests

API_KEY = "e06044136181638a95ba3accf3c45aeb"

def get_date(place, forecast_days, kind):
    url = f"api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

