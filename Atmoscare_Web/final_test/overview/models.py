from django.db import models

# Create your models here.
class userHealthRecord(models.Model):
	userID = models.IntegerField(primary_key=True)
	Gender = models.CharField(max_length=10)
	Age = models.SmallIntegerField()
	HT = models.CharField(max_length=1)
	DM = models.CharField(max_length=1)
	DysLip = models.CharField(max_length=1)
	Asthma = models.CharField(max_length=1)
	HF = models.CharField(max_length=1)
	Stroke = models.CharField(max_length=1)
	AF = models.CharField(max_length=1)
	Painkiller = models.CharField(max_length=1,default="0")
	zipcode = models.PositiveSmallIntegerField(default=0,null=False)


	def __str__(self):
		return str(self.userID)


class weatherPicture(models.Model):
 	name = models.CharField(max_length=20)
 	picture = models.CharField(max_length=10)

 	def __str__(self):
 		return str(self.name)

 
class lonLatData(models.Model):
	city = models.CharField(max_length=5)
	town = models.CharField(max_length=5)
	code = models.PositiveSmallIntegerField()
	lon  = models.DecimalField(max_digits=11, decimal_places=7)
	lat  = models.DecimalField(max_digits=10, decimal_places=7)

	def __str__(self):
 		return str(self.code)


class suggestions(models.Model):
	gender     = models.CharField(max_length=10,null=True)
	age        = models.SmallIntegerField(default=0)
	minTemp    = models.SmallIntegerField()
	maxTemp    = models.SmallIntegerField()
	weather    = models.CharField(max_length=20)
	minPM25    = models.PositiveSmallIntegerField()
	maxPM25    = models.PositiveSmallIntegerField()
	suggestion = models.CharField(max_length=80)

	def __str__(self):
 		return str(self.suggestion)

