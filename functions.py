from timezonefinder import TimezoneFinder
from main import * 
from geopy.geocoders import Nominatim

def getWeather(textfield):
    location 
    city = textfield.get()
    geolocator = Nominatim(user_agent="geoapiExercices")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitute, lat=location.latitude)
    print(result)