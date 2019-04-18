#coding=utf-8
from urllib.request import urlopen
from math import radians, cos, sin, asin, sqrt  
import json


def PM25(longitude,latitude):
	#Site's lon lat
	#url = "http://opendata.epa.gov.tw/ws/Data/AQXSite/?$orderby=SiteName&$skip=0&$top=1000&format=json"
	#response = urlopen(url).read()
	#data = json.loads(response.decode('utf-8'))
	response = open('siteName.json', encoding="utf-8").read()
	data = json.loads(response)

	#PM2.5 value
	url2 = "http://opendata2.epa.gov.tw/AQX.json"
	response2 = urlopen(url2).read()
	PM_data = json.loads(response2.decode('utf-8'))


	#the lon and lat of userLocation
	userLon = longitude			#ex. 121.435892
	userLat = latitude			#ex. 25.0831066

	Denominator = 0.0 
	numerator = 0.0
	LocationPM25 = 0
	siteCount = 0

	for i in range(len(data)):
		SiteName = data[i]["SiteName"]
		Lon = data[i]["TWD97Lon"]
		Lat = data[i]["TWD97Lat"]


		distance = haversine(userLon,userLat,Lon,Lat)
		distance = float(distance)

		if distance < 30.0 :
			siteCount += 1
			for j in range(len(PM_data)):
				PM_SiteName = PM_data[j]["SiteName"]
				#connect PM2.5 with site's lat lon
				if PM_SiteName == SiteName:
					pm25 = PM_data[j]["PM2.5"]
					if pm25 == "":break #some site doesn't have pm2.5 value
					distance = round(distance,2)

					Denominator += WiZi(pm25,distance)
					numerator += Zi(distance)

					print(SiteName+" 距離： "+str(distance)+" "+"PM2.5 : "+pm25)


	if siteCount == 0:
		LocationPM25 = "抱歉，此區域附近未設置監測站"
	else:
		LocationPM25 = Denominator / numerator
		LocationPM25 = str(round(LocationPM25,2))
		print(LocationPM25)
	return LocationPM25


#calculate lon lat distance
def haversine(lon1, lat1, lon2, lat2):
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    """  
  
    lon1 = float(lon1)
    lat1 = float(lat1)
    lon2 = float(lon2)
    lat2 = float(lat2)
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])  
  
    # haversine
    dlon = lon2 - lon1   
    dlat = lat2 - lat1   
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2  
    c = 2 * asin(sqrt(a))   
    r = 6371 # the average radius of the earth
    return (c * r * 1000)/1000 # km


#Doctor's algorithm denominator 
def WiZi(pm25,distance):
	pm25 = float(pm25)
	distance = float(distance)
	result = pm25/(distance*distance)
	return result

#Doctor's algorithm numerator
def Zi(distance):
	distance = float(distance)
	result = 1/(distance*distance)
	return result


