from .models import suggestions
def envSuggestion(nowMinTemp,nowMaxTemp,nowWeather,nowPM25):
	data = suggestions.objects.all()

	nowWeather = convertWeatherName(nowWeather)
	nowTemp = (int(nowMinTemp) + int(nowMaxTemp)) / 2
	print(nowMinTemp+" "+nowMaxTemp+" "+nowWeather+" "+nowPM25)

	advice = ""
	for i in range(len(data)):
		if nowTemp >= data[i].minTemp and nowTemp < data[i].maxTemp:
			if nowWeather == data[i].weather:
				if float(nowPM25) >= data[i].minPM25 and float(nowPM25) <= data[i].maxPM25:
					advice = data[i].suggestion
					print(advice)
	if advice == "":
		advice = "系統維護，目前無法顯示，敬請見諒！";
		
	return advice


def convertWeatherName(name):
	name = name.split("/")[4]
	name = name.split(".")[0]
	return name