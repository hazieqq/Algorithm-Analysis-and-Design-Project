from geopy.geocoders import Nominatim
import gmplot
import googlemaps
from datetime import datetime


apikey=''
gmap = gmplot.GoogleMapPlotter(4.2105, 101.9758, 14, apikey=apikey)

gmap.marker(3.0319924887507144,101.37344116244806, color='cornflowerblue') #citylink 
gmap.marker(3.112924170027219,101.63982650389863, color='cornflowerblue') #postlaju
gmap.marker(2.9441205329488325,101.7901521759029, color='cornflowerblue') #jnt
gmap.marker(3.2127230893650065,101.57467295692778, color='cornflowerblue') #gdex
gmap.marker(3.265154613796736,101.68024844550233, color='cornflowerblue') #dhl

gmap.marker(3.3615395462207878,101.56318183511695, color='red') 

gmap.marker(3.1000170516638885,101.53071480907951, color='red') 

gmap.draw('map.html')







geolocator = Nominatim(user_agent="markLocation.py")
location_CityLink = geolocator.reverse("3.0319924887507144,101.37344116244806")
location_PostLaju = geolocator.reverse("3.112924170027219,101.63982650389863")
# location_Gdex = geolocator.reverse("3.265154613796736,101.68024844550233")
# location_JNT = geolocator.reverse("2.9441205329488325,101.7901521759029")
# # location_Alep = geolocator("3.232614423087875, 101.41872423616006")
# location_DHL = geolocator.reverse("3.2127230893650065,101.57467295692778")
print(location_CityLink.address)
print(location_PostLaju.address)
