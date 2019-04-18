from django.shortcuts import render
from urllib.request import urlopen
from django.shortcuts import redirect
import threading

def index(request):
        timer = threading.Timer(0.5, download)
        timer.start()
		#session login
        hasSession = 0
        if 'userSessionID' in request.session:
            hasSession = 1
            userSessionID = request.session['userSessionID']
        return render(request,'index.html',{'hasSession':hasSession})



def download():
	
	weatherFile = urlopen("http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-005&authorizationkey=CWB-CB8F66D3-9813-4165-BE55-029133B43C79")

	#realTimeWeatherFile = urlopen("http://opendata.cwb.gov.tw/opendataapi?dataid=O-A0003-001&authorizationkey=CWB-CB8F66D3-9813-4165-BE55-029133B43C79")

	with open('./weather.xml','wb') as output:
	  output.write(weatherFile.read())

	# with open('./realTimeWeather.xml','wb') as output:
	# 	output.write(realTimeWeatherFile.read())
