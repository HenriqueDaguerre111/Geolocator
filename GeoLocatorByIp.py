import requests
from gmplot import gmplot

import requests

def getIp():
    response = requests.get('https://httpbin.org/ip')
    data = response.json()

    return data['origin']



def geolocate_ip(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()
        latitude = data['lat']
        longitude = data['lon']
        return (latitude, longitude)
    except:
        return None

location = geolocate_ip(getIp())
if location:
    latitude, longitude = location
    print(f'Latitude: {latitude}, Longitude: {longitude}')
else:
    print('Error: Unable to locate IP address')
gmap = gmplot.GoogleMapPlotter(latitude, longitude, 13, apikey='googleCloudAPIKey')

gmap.draw('map.html')
