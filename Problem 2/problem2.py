import gmplot
import requests
from map_styles import style
from dijikstra import Graph
from try1 import JohnsonAlgorithm
from Citylink.Article1.webscrapwrite import City

# coordinates of courier companies
CitylinkExpress = (3.0319924887507144, 101.37344116244806)
PosLaju = (3.112924170027219, 101.63982650389863)
GDEX = (3.265154613796736, 101.68024844550233)
JT = (2.9441205329488325, 101.7901521759029)
DHL = (3.2127230893650065, 101.57467295692778)

colorCode = ("red", "purple", "blue")

n = int(input("Enter number of customer: "))
customerOriLats = []
customerOriLngs = []
customerDestLats = []
customerDestLngs = []

for i in range(0, n):
    print('Enter origin latitudes for customer ', end=': '+'\n')
    custOriLats = float(input())
    print('Enter origin longitudes for customer ', end=': '+'\n')
    custOriLngs = float(input())
    print('Enter destination latitudes for customer ', end=': '+'\n')
    custDestLats = float(input())
    print('Enter destination longitudes for customer ', end=': '+'\n')
    custDestLngs = float(input())

    customerOriLats.append(custOriLats)
    customerOriLngs.append(custOriLngs)
    customerDestLats.append(custDestLats)
    customerDestLngs.append(custDestLngs)


courierCoorLats, courierCoorLangs = zip(
    *[CitylinkExpress, PosLaju, GDEX, JT, DHL])

courierNames = ['City-link Express', 'Pos Laju', 'GDEX', 'JT', 'DHL']


chosenCourier = []


def markLocation(gmap, courierCoorLats, courierCoorLangs, colorCode):

    for i in range(5):
        gmap.marker(courierCoorLats[i], courierCoorLangs[i],
                    color='cornflowerblue', info_window=courierNames[i])

    for i in range(0, n):
        gmap.marker(customerOriLats[i], customerOriLngs[i], color=colorCode[i])
        gmap.marker(customerDestLats[i],
                    customerDestLngs[i], color=colorCode[i])


def printBeforeDistance(customerOrilats, customerOriLngs,
                        customerDestlats, customerDestLngs):

    for i in range(0, n):

        stick1 = str(customerOriLats[i]) + "," + str(customerOriLngs[i])
        stick2 = str(customerDestLats[i]) + "," + str(customerDestLngs[i])
        url = ("https://maps.googleapis.com/maps/api/distancematrix/json?units=km&origins="
               + stick1 + "&destinations=" + stick2 + "&key=" + apikey)
        output = requests.get(url).json()
        print('Distance for Customer', i+1, '(Before):',
              output["rows"][0]["elements"][0]["distance"]["text"])


dis = []
dis1 = []
distance = []
rating = []

def printAfterDistance(customer_ori_lats, customer_ori_lngs,
                       customer_dest_lats, customer_dest_lngs,
                       courierCoorLats, courierCoorLangs, courierNames,):

    for i in range(0, n):

        stick1 = str(customerOriLats[i]) + "," + str(customerOriLngs[i])
        stick2 = str(customerDestLats[i]) + "," + str(customerDestLngs[i])

        g = Graph("", [])
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
            dis.append((float(distanceOriginToHub.split()[0])))
            dis1.append(float(distanceHubToDest.split()[0]))
        graph = [[0, dis[0], 0, dis[1], dis[2], dis[3], dis[4]],
                 [dis[0], 0, dis1[0], 0, 0, 0, 0],
                 [0, dis1[0], 0, dis1[1], dis1[2], dis1[3], dis1[4]],
                 [dis[1], 0, dis1[1], 0, 0, 0, 0],
                 [dis[2], 0, dis1[2], 0, 0, 0, 0],
                 [dis[3], 0, dis1[3], 0, 0, 0, 0],
                 [dis[4], 0, dis1[4], 0, 0, 0, 0]]
        # courier = g.dijkstra(graph, 0)
        courier = JohnsonAlgorithm(graph)
        # print(courier)
        dis.clear()
        dis1.clear()
        # for k in range(len(courierNames)):
        #     for j in range(1, len(courierNames)):
        #         if distance[k] > distance[j]:
        #             temp = distance[j]
        #             distance[j] = distance[k]
        #             distance[k] = temp

        #             temp1 = courierNames[j]
        #             courierNames[j] = courierNames[k]
        #             courierNames[k] = temp1
        #     break
        courier1 = None
        if(int(courier[1]) == 1):
            courier1 = 0
        else:
            courier1 = int(courier[1])-2

        print('Closest courier hub to Customer',
              i+1, ':', courierNames[courier1])
        print('Distance for Customer', i+1, '(After):', courier[0], 'km')
        chosenCourier.append(int(courier1))
    return distance


def rateCourierHub(hubs,dis):
    percHubs = {}
    noOfHubs = len(hubs)
    totalHubs = 0
    

    for hub in hubs:
        hubs[hub] += round(hubs[hub]*100)
        percHubs[hub] = hubs[hub]

    for hub in percHubs:
        totalHubs += percHubs[hub]

    avrgHub = totalHubs/noOfHubs
    maxRating = avrgHub*2
    print("Hubs\t\t\t\tRating\t\t\tDistance")
    index = int(0)
    for i in range(n):
        for hub in percHubs:
            if percHubs[hub] > 0 and percHubs[hub] <= (maxRating/noOfHubs):
                print(hub,"\t\t\t\t1\t\t\t",round(dis[index],2))
                rating.append(1)
            elif percHubs[hub] <= ((maxRating/noOfHubs)*2):
                print(hub,"\t\t\t\t2\t\t\t",round(dis[index],2))
                rating.append(2)
            elif percHubs[hub] <= ((maxRating/noOfHubs)*3):
                print(hub,"\t\t\t3\t\t\t",round(dis[index],2))
                rating.append(3)
            elif percHubs[hub] <= ((maxRating/noOfHubs)*4):
                print(hub,"\t\t\t\t4\t\t\t",round(dis[index],2))
                rating.append(4)
            elif percHubs[hub] <= maxRating:
                print(hub,"\t\t\t\t5\t\t\t",round(dis[index],2),"KM")
                rating.append(5)
            index += 1
    return rating

# Problem 3

def recommendation(rating,distances,hubs):
    # rating = {}
    # dis ={}
    hub_name = []
    # distan = [][]
    # rated = [][]
    maximumrating = max(rating)
    min_dis = min(distances)
    total=[]
    # total2=[][]
    print(min_dis)
    print(maximumrating)
    for j in range(len(rating)):
        rating[j] = rating[j]/maximumrating*0.5

    for  k in range(len(distances)):
        distances[k] = min_dis/distances[k]*0.5

    for  l in range (len(rating)):
        total.append(rating[l]+dis[l])
        round(total[l],2)

    for i in range(n):
        for hub in hubs:
            hub_name.append(hub)

    

    index = 0
    init = 0
    for i in range(n):
        for q in range(init, init+5):
            for k in range(init, init+5):
                if total[q]>total[k]:

                    temp = total[k]
                    total[k] = total[q]
                    total[q] = temp

                    temp = hub_name[k]
                    hub_name[k] = hub_name[q]
                    hub_name[q] = temp

            index+=1
        init = index
    print("Hubs\t\t\t\tRating\t\t\t Performance Score")
    custom = 1
    for i in range(len(hub_name)):
        # print("hub name = ", hub_name[i]," - ",total[i])
        if i%5==0:

            print("--------------------------------------------------")
            print("recommnded for customer ",custom )
            custom+=1
        print(hub_name[i],"\t\t\t\t",round(total[i],2))
            # total1.append(max(total[index])) 


   
        
    
        

    





    
    
apikey = 'AIzaSyCz9ZuEqAI4Sbg0G-F91etEvlhIt1Le0d0'
# gmap = gmplot.GoogleMapPlotter(
#     4.2105, 101.9758, 14, apikey=apikey, map_styles=style())
# # question 1
# markLocation(gmap, courierCoorLats, courierCoorLangs, colorCode)

# # question 2
# printBeforeDistance(customerOriLats, customerOriLngs,
#                     customerDestLats, customerDestLngs)

# question 3
dis = printAfterDistance(customerOriLats, customerOriLngs,
                   customerDestLats, customerDestLngs,
                   courierCoorLats, courierCoorLangs, courierNames)

# print(distance)

# question 4
# gmap.plot(*distCust1BefPath, edge_width=7, color='red')
# gmap.plot(*distCust2BefPath, edge_width=7, color='purple')
# gmap.plot(*distCust3BefPath, edge_width=7, color='blue')

# for i in range(0,n):
#     custZip = (customerOriLats[i],customerOriLngs[i])
#     custDestZip = (customerDestLats[i],customerDestLngs[i])
#     gmap.directions(custZip, custDestZip)

# after algo
# for i in range(0, n):
#     custZip = (customerOriLats[i], customerOriLngs[i])
#     custDestZip = (customerDestLats[i], customerDestLngs[i])
#     # gmap.directions(custZip, chosenCourier[i])
#     gmap.directions(
#         (customerOriLats[i], customerOriLngs[i]),
#         (customerDestLats[i], customerDestLngs[i]),
#         waypoints=[
#             (courierCoorLats[chosenCourier[i]],
#              courierCoorLangs[chosenCourier[i]])
#         ]
#     )

hubs = City()
rating = rateCourierHub(hubs,dis)
# print(rating)
# print(len(rating))
recommendation(rating,dis,hubs)

# gmap.draw('map.html')
