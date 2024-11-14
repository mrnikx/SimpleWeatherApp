import datetime

def kelvin_to_celsius(kelvin):
    """Converting temperature from Kelvin to Celsius"""
    return kelvin - 273.15

def format_timestamp(timestamp):
    """Converting and formatting time into a readable format"""
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def format_weather_description(description):
    """Formatting the text of weather descriptions in the form of titles"""
    return description.capitalize()
