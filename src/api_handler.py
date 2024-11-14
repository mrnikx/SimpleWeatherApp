import requests

def get_weather_data(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    # Checking if the request is success :

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None
