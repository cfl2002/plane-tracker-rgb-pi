ZONE_HOME = {
    "tl_y": 44.985928, # Top-Left Latitude (deg) https://www.latlong.net/ the bigger the zone, the more planes you'll get
    "tl_x": -93.312035, # Top-Left Longitude (deg)
    "br_y": 44.960668, # Bottom-Right Latitude (deg)
    "br_x": -93.242340, # Bottom-Right Longitude (deg)
}
LOCATION_HOME = [
    44.971718, # Latitude (deg)
    -93.278106, # Longitude (deg)
]
TEMPERATURE_LOCATION = "xx.xxxxxx,xx.xxxxxx" #same as location home
TOMORROW_API_KEY = "xxxxxxx" # Get an API key from https://tomorrow.io they only allows 25 pulls an hour, if you reach the limit you'll need to wait until the next hour 
TEMPERATURE_UNITS = "imperial" #can use "metric" if you want, same for distance 
DISTANCE_UNITS = "imperial"
CLOCK_FORMAT = "12hr" #use 12hr or 24hr
MIN_ALTITUDE = 1500 #feet
BRIGHTNESS = 100
BRIGHTNESS_NIGHT = 50
NIGHT_BRIGHTNESS = False #True for on False for off
NIGHT_START = "22:00" #dims screen between these hours
NIGHT_END = "06:00"
GPIO_SLOWDOWN = 2 #depends what Pi you have I use 2 for Pi 3 and 1 for Pi Zero
JOURNEY_CODE_SELECTED = "xxx" #your home airport code
JOURNEY_BLANK_FILLER = " ? " #what to display if theres no airport code
HAT_PWM_ENABLED = False #only if you have soldered the PWM bridge use False if you didn't
FORECAST_DAYS = 3 #today plus the next two days
