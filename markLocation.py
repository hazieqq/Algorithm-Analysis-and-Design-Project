from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="markLocation.py")
location_CityLink = geolocator.reverse("3.0319924887507144,101.37344116244806")
location_PostLaju = geolocator.reverse("3.112924170027219,101.63982650389863")
location_Gdex = geolocator.reverse("3.265154613796736,101.68024844550233")
location_JNT = geolocator.reverse("2.9441205329488325,101.7901521759029")
# location_Alep = geolocator.reverse("3.232614423087875, 101.41872423616006")
location_DHL = geolocator.reverse("3.2127230893650065,101.57467295692778")
print(location_DHL.raw)