#coding=utf-8
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from .models import weatherPicture

#weatherForecast
def weather(userCity):

	result = dict()

	#if we adopt the way of internet link,which has a flaw is slow sleep 
	url = urlopen("http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-005&authorizationkey=CWB-CB8F66D3-9813-4165-BE55-029133B43C79")
	url = open('weather.xml', encoding="utf-8").read()
	soup = BeautifulSoup(url,"html.parser")

	#update time
	update = soup.find('update').text
	update = update.split("T")
	update = update[0]+" "+update[1][:8]

	location = soup.findAll("location")
	for i in range(22):
		locationName = location[i].find('locationname').text
		if locationName == userCity:
			#today
			weatherName = location[i].findAll('weatherelement')[0].findAll('time')[1].find('parametername').text
			picture     = convertWeather(weatherName)
			#tomorrow
			weatherName1 = location[i].findAll('weatherelement')[0].findAll('time')[3].find('parametername').text
			picture1     = convertWeather(weatherName1)
			#the day after tomorrow
			weatherName2 = location[i].findAll('weatherelement')[0].findAll('time')[5].find('parametername').text
			picture2     = convertWeather(weatherName2)
			#three days from now
			weatherName3 = location[i].findAll('weatherelement')[0].findAll('time')[7].find('parametername').text
			picture3     = convertWeather(weatherName3)


			date = location[i].findAll('weatherelement')[1].findAll('time')[1].find('starttime').text #today
			date = convertDate(date)
			week = convertWeek(date.weekday())

			date1 = location[i].findAll('weatherelement')[1].findAll('time')[3].find('starttime').text #tomorrow
			date1 = convertDate(date1)
			week1 = convertWeek(date1.weekday())

			date2 = location[i].findAll('weatherelement')[1].findAll('time')[5].find('starttime').text #the day after tomorrow
			date2 = convertDate(date2)
			week2 = convertWeek(date2.weekday())

			date3 = location[i].findAll('weatherelement')[1].findAll('time')[7].find('starttime').text #three days from now
			date3 = convertDate(date3)
			week3 = convertWeek(date3.weekday())

			locationMaxT  = location[i].findAll('weatherelement')[1].findAll('time')[1].find('parametername').text #today
			locationMaxT1 = location[i].findAll('weatherelement')[1].findAll('time')[3].find('parametername').text #tomorrow
			locationMaxT2 = location[i].findAll('weatherelement')[1].findAll('time')[5].find('parametername').text #the day after tomorrow
			locationMaxT3 = location[i].findAll('weatherelement')[1].findAll('time')[6].find('parametername').text #three days from now
			
			locationMinT = location[i].findAll('weatherelement')[2].findAll('time')[1].find('parametername').text
			locationMinT1 = location[i].findAll('weatherelement')[2].findAll('time')[3].find('parametername').text
			locationMinT2 = location[i].findAll('weatherelement')[2].findAll('time')[5].find('parametername').text
			locationMinT3 = location[i].findAll('weatherelement')[2].findAll('time')[7].find('parametername').text

			result = {'week':week,'week1':week1,'week2':week2,'week3':week3,\
					  'locationMaxT':locationMaxT,'locationMaxT1':locationMaxT1,'locationMaxT2':locationMaxT2,'locationMaxT3':locationMaxT3,\
					  'locationMinT':locationMinT,'locationMinT1':locationMinT1,'locationMinT2':locationMinT2,'locationMinT3':locationMinT3,
					  'picture':picture,'picture1':picture1,'picture2':picture2,'picture3':picture3,
					  'update':update}
			return result
	



def convertDate(dateTemp):
	dateTemp = dateTemp.split('T')[0]
	dateTemp = datetime.strptime(dateTemp, "%Y-%m-%d")
	return dateTemp




def convertWeek(x):
    return {
        0: "一",
        1: "二",
        2: "三",
        3: "四",
        4: "五",
        5: "六",
        6: "日",
    }[x]


def convertWeather(temp):
	weatherName = weatherPicture.objects.filter(name=temp)
	Picture = weatherName[0].picture
	return "/static/images/weather-icon/"+Picture+".png"
