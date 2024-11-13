import requests

def fetch_location():
    # User location
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        city = data.get('city')
        country = data.get('country')
        location = f"{city}, {country}"
    except Exception as e:
        print(f"Error getting location: {e}")
        location = "NA"
        
    return location


