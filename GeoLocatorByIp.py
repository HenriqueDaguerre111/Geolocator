import requests
from gmplot import gmplot

def geolocate_ip(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()
        latitude = data['lat']
        longitude = data['lon']
        return (latitude, longitude)
    except:
        return None
ip_address = 'ip'
location = geolocate_ip(ip_address)
if location:
    latitude, longitude = location
    print(f'Latitude: {latitude}, Longitude: {longitude}')
else:
    print('Error: Unable to locate IP address')
gmap = gmplot.GoogleMapPlotter(latitude, longitude, 13, apikey='googleCloudAPIKey')

gmap.draw('map.html')
