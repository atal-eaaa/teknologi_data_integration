import requests
import pandas as pd
from api_key import my_key

BASE_URL = "https://api.nasa.gov/insight_weather/"

def get_latest_weather():
    """Fetch the latest weather data from Mars."""
    params = {"api_key": my_key, "feedtype": "json", "ver": "1.0"}
    response = requests.get(BASE_URL, params=params)
    return handle_api_response(response)

def handle_api_response(response):
    """Handle API response and return data or raise an error."""
    if response.status_code == 200:
        return response.json()
    else:
        # Raise an exception if the status code is not 200
        raise Exception(f"API request failed with status code {response.status_code}")



if __name__ == "__main__":
    try:
        weather_data = get_latest_weather()
        latest_days = weather_data.get('sol_keys', [])

        print(weather_data)
    
    except Exception as e:
        print(f"Error fetching weather data: {e}")