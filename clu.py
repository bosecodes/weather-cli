import argparse
import datetime
import sys

import pyowm  # this is an openweathermaps based package used to access weather info
from pyowm.uvindexapi30 import uv_client, uvindex # this package will be used to access details wrt the UV Index at a location


def find_weather(args):
    owm = pyowm.OWM("e9f1c4da2abce2e550f34cf588b1cc34")
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(args.city)
        w = observation.weather
        temp = w.temperature('celsius')
        status = w.detailed_status
        humidity = w.humidity
        pressure = w.pressure['press']
        temperature = str(int(temp['temp']))+" degrees Celcius"
        windSpeed = str(w.wind()['speed'])
        windDegree = str(w.wind()['deg'])
        return "\nDetailed Weather Updates::: " + args.city.upper() + "\nHumidity: " + str(humidity) + "\nPressure: " + str(pressure) + "\nTemperature: " + str(temperature) + "\nWind Speed: " + windSpeed + "\nWind Degree: " + windDegree
    except:
        return "No city with that name found" # if the user enters a city which is not present, or enters a wrong name 
        # the exception gets handled successfully


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type = str, default = "Bangalore", help = "This is an app that helps find weather info for a user request.")
    #parser.add_argument('--o', type = str, default = "add", help = "THis is a utility for weather info")

    args = parser.parse_args()

    sys.stdout.write(str(find_weather(args))+ "\n\n")
