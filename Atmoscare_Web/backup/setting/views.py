# -*- coding: utf-8 -*-
from django.shortcuts import render
from overview.models import userHealthRecord
from django.shortcuts import redirect
import csv

def settings(request):
	if 'userSessionID' in request.session:
		userSessionID = request.session['userSessionID']
		userRecord = userHealthRecord.objects.get(pk=userSessionID)
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
		userCity = zipDict['city']
		userTown = zipDict['town']

		#done
		userGender_done = convertGender(userGender)
		userHT_done = convertDone(userRecord.HT)
		userDM_done = convertDone(userRecord.DM)
		userDysLip_done = convertDone(userRecord.DysLip)
		userAsthma_done = convertDone(userRecord.Asthma)
		userHF_done = convertDone(userRecord.HF)
		userStroke_done = convertDone(userRecord.Stroke)
		userAF_done = convertDone(userRecord.AF)
		userPainkiller_done = convertDone(userRecord.Painkiller)

		#checked
		userHT_check = convertCheck(userRecord.HT)
		userDM_check = convertCheck(userRecord.DM)
		userDysLip_check = convertCheck(userRecord.DysLip)
		userAsthma_check = convertCheck(userRecord.Asthma)
		userHF_check = convertCheck(userRecord.HF)
		userStroke_check = convertCheck(userRecord.Stroke)
		userAF_check = convertCheck(userRecord.AF)
		userPainkiller_check = convertCheck(userRecord.Painkiller)
	
	if request.POST.get('userInfo',''):
		userGender = request.POST['Gender']
		userAge = request.POST['Age']
		userZipCode = request.POST['zipcode']

		userData = userHealthRecord.objects.filter(userID=userSessionID)
		userData.update(Gender=userGender)
		userData.update(Age=userAge)
		userData.update(zipcode=userZipCode)
		return redirect("http://www.atmoscareplus.com/settings")

	if request.POST.get('healthUpdate',''):
		userHT = request.POST['HT']
		userDM = request.POST['DM']
		userDysLip = request.POST['DysLip']
		userAsthma = request.POST['Asthma']
		userHF = request.POST['HF']
		userStroke = request.POST['Stroke']
		userAF = request.POST['AF']
		userPainkiller = request.POST['Painkiller']

		#Update Data
		userData = userHealthRecord.objects.filter(userID=userSessionID)
		userData.update(HT=userHT)
		userData.update(DM=userDM)
		userData.update(DysLip=userDysLip)
		userData.update(Asthma=userAsthma)
		userData.update(HF=userHF)
		userData.update(Stroke=userStroke)
		userData.update(AF=userAF)
		userData.update(Painkiller=userPainkiller)
		return redirect("http://www.atmoscareplus.com/settings")

	return render(request,'setting.html',{'userSessionID':userSessionID,
		'userGender':userGender,'userGender_done':userGender_done,
		'userAge':userAge,
		'userHT':userHT,'userDM':userDM,'userDysLip':userDysLip,'userAsthma':userAsthma,'userHF':userHF,'userStroke':userStroke,'userAF':userAF,'userPainkiller':userPainkiller,
		'userHT_done':userHT_done,'userDM_done':userDM_done,'userDysLip_done':userDysLip_done,'userAsthma_done':userAsthma_done,'userHF_done':userHF_done,'userStroke_done':userStroke_done,'userAF_done':userAF_done,'userPainkiller_done':userPainkiller_done,
		'checkHT':userHT_check,'checkDM':userDM_check,'checkDysLip':userDysLip_check,'checkAsthma':userAsthma_check,'checkHF':userHF_check,'checkStroke':userStroke_check,'checkAF':userAF_check,'checkPainkiller':userPainkiller_check,
		'userCity':userCity,'userTown':userTown})

def zipCode(code):
	result = dict()
	lon = 0.0
	lat = 0.0
	f = open('LonLatData.csv', 'r', encoding="utf-8")  
	data = csv.DictReader(f)

	for row in data:
		zipcode = row['code']
		if int(code) == int(zipcode):
			lon = row['lon']
			lat = row['lat']
			city = row['city']
			town = row['county']
			result={'lon':lon,'lat':lat,'city':city,'town':town}
	f.close()

	return result



def convertDone(userRecord):
	temp = ""
	if userRecord == "1":
		temp = "done"
	else:
		temp = "0"
	return temp

def convertCheck(userRecord):
	temp = ""
	if userRecord == "1":
		temp = "checked"
	else:
		temp = ""
	return temp


def convertGender(userRecord):
	temp = ""
	if userRecord == "M":
		temp = "男"
	else:
		temp = "女"
	return temp


