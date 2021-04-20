from geopy.geocoders import Nominatim
import gmplot
import googlemaps
import requests
import urllib, json


apikey='AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI'
gmap = gmplot.GoogleMapPlotter(4.2105, 101.9758, 14, apikey=apikey)

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
    (3.0319924887507144,101.37344116244806),
    (3.112924170027219,101.63982650389863),
    (3.265154613796736,101.68024844550233),
    (2.9441205329488325,101.7901521759029),
    (3.2127230893650065,101.57467295692778)
])


hub = ["citylink","postlaju","gdex","j&t","dhl"]


for i in range(3):
    stick1 = str(customer_ori_lats[i]) + "," + str(customer_ori_lngs[i])
    stick2 = str(customer_dest_lats[i]) + "," + str(customer_dest_lngs[i])
    url = ("https://maps.googleapis.com/maps/api/distancematrix/json?&origins="
            +stick1
            +"&destinations="
            +stick2
            +"&key=AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI"
            )
    output = requests.get(url).json()
    
    # print(output)
    print(output["rows"][0]["elements"][0]["distance"]["text"])


shortest=[]
hubshortest=[]
for i in range(3):
    stick1 = str(customer_ori_lats[i]) + "," + str(customer_ori_lngs[i])
    stick2 = str(customer_dest_lats[i]) + "," + str(customer_dest_lngs[i])
    distance=[]
    for j in range(5):
        stick3 = str(hub_ori_lats[j]) + "," + str(hub_ori_lngs[j])
        url = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
            +stick1
            +"&destinations="
            +stick3
            +"&key=AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI"
            )
        url1 = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
            +stick3
            +"&destinations="
            +stick2
            +"&key=AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI"
            )
        output = requests.get(url).json()
        output1 = requests.get(url1).json()
        distanceOriginToHub = str(output["rows"][0]["elements"][0]["distance"]["text"])
        distanceOriginToHub1 = str(output1["rows"][0]["elements"][0]["distance"]["text"])
        distance.append((float(distanceOriginToHub.split()[0])) + float(distanceOriginToHub1.split()[0]))

    for k in range(0,len(hub)):
        for j in range(1,len(hub)):
            if distance[k] > distance[j]:
                temp = distance[j]
                distance[j] = distance[k]
                distance[k] = temp

                temp1 = hub[j]
                hub[j] = hub[k]
                hub[k] = temp1
    shortest.append(distance[0])
    hubshortest.append(hub[0])
print(shortest)
print(hubshortest)

    











geolocator = Nominatim(user_agent="markLocation.py")
location_CityLink = geolocator.reverse("3.0319924887507144,101.37344116244806")
location_PostLaju = geolocator.reverse("3.112924170027219,101.63982650389863")
# location_Gdex = geolocator.reverse("3.265154613796736,101.68024844550233")
# location_JNT = geolocator.reverse("2.9441205329488325,101.7901521759029")
# # location_Alep = geolocator("3.232614423087875, 101.41872423616006")
# location_DHL = geolocator.reverse("3.2127230893650065,101.57467295692778")
# print(location_CityLink.address)
# print(location_PostLaju.address)
