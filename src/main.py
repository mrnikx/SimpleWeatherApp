import api_handler
from config import API_KEY

# Add your API key in config.py

def display_weather_info(city_name):
    weather_data = api_handler.get_weather_data(city_name, API_KEY)
    
    # If the data was received successfully

    if weather_data:
        main_info = weather_data['main']
        weather_desc = weather_data['weather'][0]['description']
        
        print(f"Weather in {city_name.capitalize()}:")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Temperature: {main_info['temp']}°C")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Feels like: {main_info['feels_like']}°C")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Humidity: {main_info['humidity']}%")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(f"Condition: {weather_desc.capitalize()}")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    print('')
    display_weather_info(city)
