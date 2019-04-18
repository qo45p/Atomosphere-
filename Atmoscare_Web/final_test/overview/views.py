#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from overview.models import userHealthRecord,lonLatData
import csv
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import json
import time
from .weatherForecast import weather
from .pm25 import PM25
from .suggestion import envSuggestion



def overview(request):
	return render(request,'overview.html',{
	})



# check the table of risk 
def risk(request):
	#url version
	#url = "http://winterolympicsmedals.com/medals.csv"
	#response = urlopen(url).read()
	#data = csv.DictReader(response)
	userStrokeRisk = 0
	userHFRisk = 0
	userAFRisk = 0
	userHeartRisk = 0
	userOverallRisk = 0
	userGivenID = 0
	LocationPM25 = 0.0
	week1 = ""
	week2 = ""
	week3 = ""
	maxTemp  = 0 
	maxTemp1 = 0
	maxTemp2 = 0
	maxTemp3 = 0
	minTemp  = 0
	minTemp1 = 0
	minTemp2 = 0
	minTemp3 = 0
	picture  = ""
	picture1 = ""
	picture2 = ""
	picture3 = ""
	update   = ""
	advice   = ""
	
	#delete session
	#request.session.modified = True
	#del request.session['userSessionID']
	
	

	if 'userSessionID' in request.session:
			userSessionID = request.session['userSessionID']
			userRecord = userHealthRecord.objects.get(pk=userSessionID)
			userGivenID = userSessionID
			userGender = userRecord.Gender
			userAge = str(userRecord.Age)
			userHT = userRecord.HT
			userDM = userRecord.DM
			userDysLip = userRecord.DysLip
			userAsthma = userRecord.Asthma
			userHF = userRecord.HF
			userStroke = userRecord.Stroke
			userAF = userRecord.AF
			userPainkiller = userRecord.Painkiller
			userZipCode = userRecord.zipcode

			zipDict = zipCode(userZipCode)

			LocationPM25 = PM25(zipDict['lon'],zipDict['lat'])
			LocationWeather = weather(zipDict['city'])
			week1 = LocationWeather['week1']
			week2 = LocationWeather['week2']
			week3 = LocationWeather['week3']
			maxTemp  = LocationWeather['locationMaxT']
			maxTemp1 = LocationWeather['locationMaxT1']
			maxTemp2 = LocationWeather['locationMaxT2']
			maxTemp3 = LocationWeather['locationMaxT3']
			minTemp  = LocationWeather['locationMinT']
			minTemp1 = LocationWeather['locationMinT1']
			minTemp2 = LocationWeather['locationMinT2']
			minTemp3 = LocationWeather['locationMinT3']
			picture  = LocationWeather['picture']
			picture1 = LocationWeather['picture1']
			picture2 = LocationWeather['picture2']
			picture3 = LocationWeather['picture3']
			update   = LocationWeather['update']

			nowTemp  = (int(maxTemp) + int(minTemp))/2
			measureRisk(userGender,userAge,userHT,userDM,userDysLip,userAsthma,userHF,userStroke,userAF,userPainkiller,LocationPM25,nowTemp)
			advice   = envSuggestion(minTemp,maxTemp,picture,LocationPM25)


	#userID search version  
	if request.POST.get('userID','') and request.method=='POST':
		userGivenID = request.POST['userID']
		try:
			userRecord = userHealthRecord.objects.get(pk=userGivenID)
			userGender = userRecord.Gender
			userAge = str(userRecord.Age)
			userHT = userRecord.HT
			userDM = userRecord.DM
			userDysLip = userRecord.DysLip
			userAsthma = userRecord.Asthma
			userHF = userRecord.HF
			userStroke = userRecord.Stroke
			userAF = userRecord.AF
			userPainkiller = userRecord.Painkiller
			userZipCode = userRecord.zipcode

			zipDict = zipCode(userZipCode)

			LocationPM25 = PM25(zipDict['lon'],zipDict['lat'])
			LocationWeather = weather(zipDict['city'])
			week1 = LocationWeather['week1']
			week2 = LocationWeather['week2']
			week3 = LocationWeather['week3']
			maxTemp  = LocationWeather['locationMaxT']
			maxTemp1 = LocationWeather['locationMaxT1']
			maxTemp2 = LocationWeather['locationMaxT2']
			maxTemp3 = LocationWeather['locationMaxT3']
			minTemp  = LocationWeather['locationMinT']
			minTemp1 = LocationWeather['locationMinT1']
			minTemp2 = LocationWeather['locationMinT2']
			minTemp3 = LocationWeather['locationMinT3']
			picture  = LocationWeather['picture']
			picture1 = LocationWeather['picture1']
			picture2 = LocationWeather['picture2']
			picture3 = LocationWeather['picture3']
			update   = LocationWeather['update']

			nowTemp  = (int(maxTemp) + int(minTemp))/2
			measureRisk(userGender,userAge,userHT,userDM,userDysLip,userAsthma,userHF,userStroke,userAF,userPainkiller,LocationPM25,nowTemp)

			advice   = envSuggestion(minTemp,maxTemp,picture,LocationPM25)

			request.session['userSessionID'] = userGivenID

		except ObjectDoesNotExist:
			return redirect("https://www.atmoscareplus.com/");
		except ValueError:
			return redirect("https://www.atmoscareplus.com/");

	#enter data search version
	if 'Age' in request.POST and request.POST['Age'] != '':
		#Gender Age HT DM DysLip Asthma HF Stroke AF
		userGender = request.POST['Gender']
		userAge = request.POST['Age']
		userHT = request.POST['HT']
		userDM = request.POST['DM']
		userDysLip = request.POST['DysLip']
		userAsthma = request.POST['Asthma']
		userHF = request.POST['HF']
		userStroke = request.POST['Stroke']
		userAF = request.POST['AF']
		userPainkiller = request.POST['Painkiller']
		userZipCode = request.POST['zipcode']
		
		zipDict = zipCode(userZipCode)
		LocationPM25 = PM25(zipDict['lon'],zipDict['lat'])
		LocationWeather = weather(zipDict['city'])
		week1 = LocationWeather['week1']
		week2 = LocationWeather['week2']
		week3 = LocationWeather['week3']
		maxTemp  = LocationWeather['locationMaxT']
		maxTemp1 = LocationWeather['locationMaxT1']
		maxTemp2 = LocationWeather['locationMaxT2']
		maxTemp3 = LocationWeather['locationMaxT3']
		minTemp  = LocationWeather['locationMinT']
		minTemp1 = LocationWeather['locationMinT1']
		minTemp2 = LocationWeather['locationMinT2']
		minTemp3 = LocationWeather['locationMinT3']
		picture  = LocationWeather['picture']
		picture1 = LocationWeather['picture1']
		picture2 = LocationWeather['picture2']
		picture3 = LocationWeather['picture3']
		update   = LocationWeather['update']

		nowTemp  = (int(maxTemp) + int(minTemp))/2
		measureRisk(userGender,userAge,userHT,userDM,userDysLip,userAsthma,userHF,userStroke,userAF,userPainkiller,LocationPM25,nowTemp)
		advice   = envSuggestion(minTemp,maxTemp,picture,LocationPM25)

		#insert data to database
		global userGivenID
		userGivenID = createUserID()
		userHealthRecord.objects.create(userID=userGivenID,Gender=userGender,Age=userAge,HT=userHT,DM=userDM,DysLip=userDysLip,Asthma=userAsthma,
			HF=userHF,Stroke=userStroke,AF=userAF,Painkiller=userPainkiller,zipcode=userZipCode)

		#session login
		request.session['userSessionID'] = userGivenID
		request.session['login'] = "OK"

	# if not request.session.get('login'):
	# 	return redirect("https://www.atmoscareplus.com/");

	#risk state
	risk_dict   = RiskState(userOverallRisk,userStrokeRisk,userHFRisk,userAFRisk,userHeartRisk,LocationPM25)
	OverallState = risk_dict['OverallState']
	StrokeState = risk_dict['StrokeState']
	HFState     = risk_dict['HFState']
	AFState     = risk_dict['AFState']
	HeartState  = risk_dict['HeartState']
	PM25State   = risk_dict['PM25State']

	OverallColor = risk_dict['OverallColor']
	StrokeColor = risk_dict['StrokeColor']
	HFColor     = risk_dict['HFColor']
	AFColor     = risk_dict['AFColor']
	HeartColor  = risk_dict['HeartColor']
	PM25Color   = risk_dict['PM25Color']

	global userStrokeRisk
	global userHFRisk
	global userAFRisk
	global userHeartRisk
	global userOverallRisk

	return render(request,'overview.html',{'OverallRisk':userOverallRisk,'OverallState':OverallState,'OverallColor':OverallColor,'StrokeRisk':userStrokeRisk,'HFRisk':userHFRisk,'AFRisk':userAFRisk,'userHeartRisk':userHeartRisk,
		'StrokeState':StrokeState,'HFState':HFState,'AFState':AFState,'HeartState':HeartState,'StrokeColor':StrokeColor,'HFColor':HFColor,'AFColor':AFColor,'HeartColor':HeartColor,
		'PM25State':PM25State,'PM25Color':PM25Color,
		'userGivenID':userGivenID,'PM25':LocationPM25,'week1':week1,'week2':week2,'week3':week3,
		'maxTemp':maxTemp,'maxTemp1':maxTemp1,'maxTemp2':maxTemp2,'maxTemp3':maxTemp3,
		'minTemp':minTemp,'minTemp1':minTemp1,'minTemp2':minTemp2,'minTemp3':minTemp3,
		'picture':picture,'picture1':picture1,'picture2':picture2,'picture3':picture3,
		'update':update,'suggestion':advice});



#measure Risk function
def measureRisk(userGender,userAge,userHT,userDM,userDysLip,userAsthma,userHF,userStroke,userAF,userPainkiller,nowPM25,nowTemperature):
	#file version
	if int(userAge) >= 0 and int(userAge) <= 8:
		data = csv.DictReader(open("disease_0_8.csv", encoding="utf-8"))
	elif int(userAge) >= 9 and int(userAge) <= 16:
		data = csv.DictReader(open("disease_9_16.csv", encoding="utf-8"))
	elif int(userAge) >= 17 and int(userAge) <= 25:
		data = csv.DictReader(open("disease_17_25.csv", encoding="utf-8"))
	elif int(userAge) >= 26 and int(userAge) <= 35:
		data = csv.DictReader(open("disease_26_35.csv", encoding="utf-8"))
	elif int(userAge) >= 36 and int(userAge) <= 45:
		data = csv.DictReader(open("disease_36_45.csv", encoding="utf-8"))
	elif int(userAge) >= 46 and int(userAge) <= 55:
		data = csv.DictReader(open("disease_46_55.csv", encoding="utf-8"))
	elif int(userAge) >= 56 and int(userAge) <= 65:
		data = csv.DictReader(open("disease_56_65.csv", encoding="utf-8"))
	elif int(userAge) >= 66 and int(userAge) <= 200:
		data = csv.DictReader(open("disease_66_200.csv", encoding="utf-8"))
	
	result_list = list()


	# look up the result of the risk table
	result_list = [x for x in data if x["Gender"] == userGender and int(x["yearMin"]) <= int(userAge) and int(x["yearMax"]) >= int(userAge) and 
			  x["HT"] == userHT and x["DM"] == userDM and x["DysLip"] == userDysLip and x["Asthma"] == userAsthma and 
			  x["HF"] == userHF and x["Stroke"] == userStroke and x["AF"] == userAF and x["Painkiller"] == userPainkiller and
			  float(x["pm25Min"]) <= float(nowPM25) and float(x["pm25Max"]) > float(nowPM25) and
			  float(x["temperatureMin"]) <= float(nowTemperature) and float(x["temperatureMax"]) > float(nowTemperature)
			  ]
	

	
	print(result_list)
	for userRisk in result_list:
		global userStrokeRisk
		global userHFRisk
		global userAFRisk
		global userHeartRisk
		global userOverallRisk
		userStrokeRisk = float(userRisk['strokeRisk'])

		userHFRisk = float(userRisk['hfRisk'])
		userAFRisk = float(userRisk['afRisk'])
		userHeartRisk = float(userRisk['heartAttackRisk'])
		userOverallRisk = float(userRisk['overall'])
		if userStrokeRisk > 1:
			userStrokeRisk = 1
		if userHFRisk > 1:
			userHFRisk = 1
		if userHeartRisk > 1:
			userHeartRisk = 1
		if userOverallRisk > 1:
			userOverallRisk = 1



#Risk State
def RiskState(userOverallRisk,userStrokeRisk,userHFRisk,userAFRisk,userHeartRisk,PM25):
	result = dict()

	OverallState = ""
	OverallColor = ""
	if userOverallRisk <= 0.5:
		OverallState = "良好"
		OverallColor="#4DB78A"
	elif userOverallRisk > 0.5 and userOverallRisk <= 0.75:
		OverallState = "不良"
		OverallColor="#F15A24"
	else:
		OverallState = "危險"
		OverallColor="#c62828"

	StrokeState = ""
	StrokeColor = ""
	if userStrokeRisk <= 0.5:
		StrokeState = "良好"
		StrokeColor="#4DB78A"
	elif userStrokeRisk > 0.5 and userStrokeRisk <= 0.75:
		StrokeState = "不良"
		StrokeColor="#F15A24"
	else:
		StrokeState = "危險"
		StrokeColor="#c62828"

	HFState = ""
	HFColor = ""
	if userHFRisk <= 0.5:
		HFState = "良好"
		HFColor = "#4DB78A"
	elif userHFRisk > 0.5 and userHFRisk <= 0.75:
		HFState = "不良"
		HFColor = "#F15A24"
	else:
		HFState = "危險"
		HFColor = "#c62828"

	AFState = ""
	AFColor = ""
	if userAFRisk <= 0.5:
		AFState = "良好"
		AFColor = "#4DB78A"
	elif userAFRisk > 0.5 and userAFRisk <= 0.75:
		AFState = "不良"
		AFColor = "#F15A24"
	else:
		AFState = "危險"
		AFColor = "#c62828"

	HeartState = ""
	HeartColor = ""
	if userHeartRisk <= 0.5:
		HeartState = "良好"
		HeartColor = "#4DB78A"
	elif userHeartRisk > 0.5 and userHeartRisk <= 0.75:
		HeartState = "不良"
		HeartColor = "#F15A24"
	else:
		HeartState = "危險"
		HeartColor = "#c62828"

	PM25State = ""
	PM25Color = ""
	PM25 = float(PM25)
	if PM25 <= 35.0:
		PM25State = "低"
		PM25Color = "#4DB78A"
	elif PM25 > 35.0 and PM25 <= 54.0:
		PM25State = "中"
		PM25Color = "F15A24"
	elif PM25 > 54.0 and PM25 <= 70.0:
		PM25State = "高"
		PM25Color = "#FF1D25"
	else:
		PM25State = "非常高"
		PM25Color = "#CE30FF"

	result = {'OverallState':OverallState,'OverallColor':OverallColor,
			  'StrokeState':StrokeState,'StrokeColor':StrokeColor,
			  'HFState':HFState,'HFColor':HFColor,
			  'AFState':AFState,'AFColor':AFColor,
			  'HeartState':HeartState,'HeartColor':HeartColor,
			  'PM25State':PM25State,'PM25Color':PM25Color}
	return result


# timeStamp as userID
def createUserID():
	now = int(time.time())
	now = str(now)
	return now[2:len(now)]



# use zipCode search lon lat
def zipCode(userZipCode):
	result = dict()
	lon = 0.0
	lat = 0.0

	row   = lonLatData.objects.filter(code=userZipCode)
	lon   = row[0].lon
	lat   = row[0].lat
	city  = row[0].city
	town  = row[0].town
			
	result={'lon':lon,'lat':lat,'city':city,'town':town}

	return result

