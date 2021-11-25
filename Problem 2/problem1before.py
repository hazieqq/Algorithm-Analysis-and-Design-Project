import gmplot
import requests
from map_styles import style

apikey = 'YOUR API'
courierNames = ['City-link Express', 'Pos Laju', 'GDEX', 'JT', 'DHL']
gmap1 = gmplot.GoogleMapPlotter(
        4.2105, 101.9758, 14, apikey=apikey, map_styles=style())

def markLocation1(courierCoorLats, courierCoorLangs, colorCode):
    
    for i in range(5):
        gmap1.marker(courierCoorLats[i], courierCoorLangs[i],color='cornflowerblue', info_window=courierNames[i])

    gmap1.draw('map2.html')

def printbefore(custZip,custDestZip):
    gmap1.directions(custZip, custDestZip)
    


