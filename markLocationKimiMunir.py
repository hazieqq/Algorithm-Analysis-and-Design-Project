from geopy.geocoders import Nominatim
import gmplot
# import googlemaps
import requests
import re

apikey='AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI'
gmap = gmplot.GoogleMapPlotter(4.2105, 101.9758, 14, apikey)

gmap.marker(3.0319924887507144,101.37344116244806, color='cornflowerblue') #citylink 
gmap.marker(3.112924170027219,101.63982650389863, color='cornflowerblue') #postlaju
gmap.marker(2.9441205329488325,101.7901521759029, color='cornflowerblue') #jnt
gmap.marker(3.2127230893650065,101.57467295692778, color='cornflowerblue') #gdex
gmap.marker(3.265154613796736,101.68024844550233, color='cornflowerblue') #dhl

gmap.marker(3.3615395462207878,101.56318183511695, color='red') #customer 1

gmap.marker(3.1000170516638885,101.53071480907951, color='red') #customer 1

gmap.marker(3.049398375759954,101.58546611160301, color='purple') #customer 2
gmap.marker(3.227994355250716,101.42730357605375, color='purple') #customer 2

gmap.draw('map.html')

customer_ori_lats, customer_ori_lngs = zip(*[
    (3.3615395462207878,101.56318183511695),
    (3.049398375759954,101.58546611160301),
    (3.141855957281073,101.76158583424586)
])

customer_dest_lats, customer_dest_lngs = zip(*[
    (3.1000170516638885,101.53071480907951),
    (3.227994355250716,101.42730357605375),
    (2.9188704151716256,101.65251821655471)
])

hub_ori_lats, hub_ori_lngs = zip(*[
    (3.0319924887507144, 101.37344116244806),
    (3.112924170027219, 101.63982650389863),
    (3.265154613796736, 101.68024844550233),
    (2.9441205329488325, 101.7901521759029),
    (3.2127230893650065, 101.57467295692778)
])

hub = ["Port Klang(CITY-LINK)", "Petaling Jaya(Pos Laju)", "Batu Caves(GDEX)", "Kajang(J&T)", "Sungai Buloh(DHL)"]

for i in range(3):
    stick1 = str(customer_ori_lats[i]) + "," + str(customer_ori_lngs[i])
    stick2 = str(customer_dest_lats[i]) + "," + str(customer_dest_lngs[i])
    url = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
            +stick1
            +"&destinations="
            +stick2
            +"&key=AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI"
            )
    output = requests.get(url).json()
    print(output["rows"][0]["elements"][0]["distance"]["text"])

distance = [0]*5
result1 = [0]*1
result2 = [0]*1
for i in range(3):
    for j in range(5):
        stick1 = str(customer_ori_lats[i]) + "," + str(customer_ori_lngs[i])
        stick2 = str(hub_ori_lats[j]) + "," + str(hub_ori_lngs[j])
        stick3 = str(customer_dest_lats[i]) + "," + str(customer_dest_lngs[i])      
        url = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
                +stick1
                +"&destinations="
                +stick2
                +"&key=AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI"
                )
        output = requests.get(url).json()
        s = output["rows"][0]["elements"][0]["distance"]["text"]
        result1 = re.findall(r"[-+]?\d*\.\d+|\d+", s)
        temp1 = float(result1[0])
        url = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
                +stick2
                +"&destinations="
                +stick3
                +"&key=AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI"
                )
        output = requests.get(url).json()
        s = output["rows"][0]["elements"][0]["distance"]["text"]
        result2 = re.findall(r"[-+]?\d*\.\d+|\d+", s)
        temp2 = float(result2[0])
        distance[j] = temp1 + temp2
    else:
        print(distance)
        smallest = min(distance)
        min_index = distance.index(smallest)
        print("Least distance for customer", i+1, "is", smallest, "which is using hub", hub[min_index] + "\n")

geolocator = Nominatim(user_agent="markLocation.py")
location_CityLink = geolocator.reverse("3.0319924887507144,101.37344116244806")
location_PostLaju = geolocator.reverse("3.112924170027219,101.63982650389863")
location_Gdex = geolocator.reverse("3.265154613796736,101.68024844550233")
location_JNT = geolocator.reverse("2.9441205329488325,101.7901521759029")
# location_Alep = geolocator("3.232614423087875, 101.41872423616006")
location_DHL = geolocator.reverse("3.2127230893650065,101.57467295692778")
print(location_CityLink.address)
print(location_PostLaju.address)
