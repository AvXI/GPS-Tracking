from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import datetime
import time

# Define a function to get the current location coordinates
def get_current_location():
    geolocator = Nominatim(user_agent='gps_tracker')
    location = geolocator.geocode('')
    return (location.latitude, location.longitude)

# Define the target location coordinates
target_location = (40.7128, -74.0060)

# Define a function to calculate the distance between two locations
def calculate_distance(current_location, target_location):
    return geodesic(current_location, target_location).meters

# Define a function to log the current location and time
def log_location(current_location):
    now = datetime.now()
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')
    print(f'{current_time} - Current location: {current_location}')

# Define the tracking loop
while True:
    current_location = get_current_location()
    distance = calculate_distance(current_location, target_location)
    if distance < 50:
        # If the distance is less than 50 meters, log the location and wait for 10 seconds
        log_location(current_location)
        time.sleep(10)
    else:
        # If the distance is greater than or equal to 50 meters, wait for 60 seconds before checking again
        time.sleep(60)