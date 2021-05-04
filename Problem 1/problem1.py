import gmplot
import requests
import os

# coordinates of courier companies
cityLinkHub = (3.0319924887507144, 101.37344116244806)
posLajuHub = (3.112924170027219, 101.63982650389863)
gdexHub = (3.265154613796736, 101.68024844550233)
jntHub = (2.9441205329488325, 101.7901521759029)
dhlHub = (3.2127230893650065, 101.57467295692778)

# coordinates of customers
cust1Ori = (3.3615395462207878, 101.56318183511695)
cust1Dest = (3.1000170516638885, 101.53071480907951)
cust2Ori = (3.049398375759954, 101.58546611160301)
cust2Dest = (3.227994355250716, 101.42730357605375)
cust3Ori = (3.141855957281073, 101.76158583424586)
cust3Dest = (2.9188704151716256, 101.65251821655471)

courierCoorLats, courierCoorLangs = zip(
    *[cityLinkHub, posLajuHub, gdexHub, jntHub, dhlHub])

courierNames = ['City-link Express', 'Pos Laju', 'GDEX', 'J&T', 'DHL']


customer_ori_lats, customer_ori_lngs = zip(*[cust1Ori, cust2Ori, cust3Ori])
customer_dest_lats, customer_dest_lngs = zip(
    *[cust1Dest, cust2Dest, cust3Dest])

distCust1BefPath = zip(*[cust1Ori, cust1Dest])
distCust2BefPath = zip(*[cust2Ori, cust2Dest])
distCust3BefPath = zip(*[cust3Ori, cust3Dest])

chosenCourier = []


def markLocation(gmap, courierCoorLats, courierCoorLangs,
                 cust1Ori, cust1Dest, cust2Ori, cust2Dest, cust3Ori, cust3Dest):

    for i in range(5):
        gmap.marker(courierCoorLats[i], courierCoorLangs[i],
                    color='cornflowerblue')

    # customer 1
    gmap.marker(cust1Ori[0], cust1Ori[1], color='red')
    gmap.marker(cust1Dest[0], cust1Dest[1], color='red')

    # customer 2
    gmap.marker(cust2Ori[0], cust2Ori[1], color='purple')
    gmap.marker(cust2Dest[0], cust2Dest[1], color='purple')

    # customer 3
    gmap.marker(cust3Ori[0], cust3Ori[1], color='blue')
    gmap.marker(cust3Dest[0], cust3Dest[1], color='blue')


def printBeforeDistance(customer_ori_lats, customer_ori_lngs,
                        customer_dest_lats, customer_dest_lngs):

    for i in range(3):
        stick1 = str(customer_ori_lats[i]) + "," + str(customer_ori_lngs[i])
        stick2 = str(customer_dest_lats[i]) + "," + str(customer_dest_lngs[i])
        url = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
               + stick1 + "&destinations=" + stick2 + "&key=" + apikey)
        output = requests.get(url).json()
        print('Distance for Customer', i+1, '(Before):',
              output["rows"][0]["elements"][0]["distance"]["text"])


def printAfterDistance(customer_ori_lats, customer_ori_lngs,
                       customer_dest_lats, customer_dest_lngs,
                       courierCoorLats, courierCoorLangs, courierNames,):

    for i in range(3):
        stick1 = str(customer_ori_lats[i]) + "," + str(customer_ori_lngs[i])
        stick2 = str(customer_dest_lats[i]) + "," + str(customer_dest_lngs[i])
        distance = []
        courierNames = ['City-link Express', 'Pos Laju', 'GDEX', 'J&T', 'DHL']
        for j in range(5):
            stick3 = str(courierCoorLats[j]) + "," + str(courierCoorLangs[j])
            urlOriginToHub = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
                              + stick1 + "&destinations=" + stick3 + "&key=" + apikey)
            urlHubToDest = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
                            + stick3 + "&destinations=" + stick2 + "&key=" + apikey)
            outputOriginToHub = requests.get(urlOriginToHub).json()
            outputHubToDest = requests.get(urlHubToDest).json()
            distanceOriginToHub = str(
                outputOriginToHub["rows"][0]["elements"][0]["distance"]["text"])
            distanceHubToDest = str(
                outputHubToDest["rows"][0]["elements"][0]["distance"]["text"])
            distance.append((float(distanceOriginToHub.split()[
                            0])) + float(distanceHubToDest.split()[0]))

        for k in range(len(courierNames)):
            for j in range(1, len(courierNames)):
                if distance[k] > distance[j]:
                    temp = distance[j]
                    distance[j] = distance[k]
                    distance[k] = temp

                    temp1 = courierNames[j]
                    courierNames[j] = courierNames[k]
                    courierNames[k] = temp1
            break

        print('Closest courier hub to Customer', i+1, ':', courierNames[0])
        print('Distance for Customer', i+1, '(After):', distance[0], 'km')

        if courierNames[0] == 'City-link Express':
            chosenCourier.append(cityLinkHub)
        elif courierNames[0] == 'Pos Laju':
            chosenCourier.append(posLajuHub)

        elif courierNames[0] == 'GDEX':
            chosenCourier.append(gdexHub)

        elif courierNames[0] == 'J&T':
            chosenCourier.append(jntHub)

        elif courierNames[0] == 'DHL':
            chosenCourier.append(dhlHub)


apikey = 'AIzaSyALoQuHQws1uow3VCluraRw97xWY3dqKnI'
gmap = gmplot.GoogleMapPlotter(4.2105, 101.9758, 14, apikey=apikey)

# question 1
markLocation(gmap, courierCoorLats, courierCoorLangs,
             cust1Ori, cust1Dest, cust2Ori, cust2Dest, cust3Ori, cust3Dest)

# question 2
printBeforeDistance(customer_ori_lats, customer_ori_lngs,
                    customer_dest_lats, customer_dest_lngs)
print()

# question 3
printAfterDistance(customer_ori_lats, customer_ori_lngs,
                   customer_dest_lats, customer_dest_lngs,
                   courierCoorLats, courierCoorLangs, courierNames,)

# question 4
# gmap.plot(*distCust1BefPath, edge_width=7, color='red')
# gmap.plot(*distCust2BefPath, edge_width=7, color='purple')
# gmap.plot(*distCust3BefPath, edge_width=7, color='blue')
gmap.directions(cust1Ori, cust1Dest)
gmap.directions(cust2Ori, cust2Dest)
gmap.directions(cust3Ori, cust3Dest)

# after algo
gmap.directions(cust1Ori, chosenCourier[0])
gmap.directions(chosenCourier[0], cust1Dest)

gmap.directions(cust2Ori, chosenCourier[1])
gmap.directions(chosenCourier[1], cust2Dest)

gmap.directions(cust3Ori, chosenCourier[2])
gmap.directions(chosenCourier[2], cust3Dest)

savePath = 'Problem 1'
fileName = 'map.html'
mapHtml = os.path.join(savePath, fileName)
gmap.draw(mapHtml)
