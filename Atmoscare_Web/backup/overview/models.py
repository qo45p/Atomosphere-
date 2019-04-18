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
	createDate = models.DateTimeField(auto_now_add=True,auto_now=False)
	endLoginDate = models.DateTimeField(auto_now = True)


	def __str__(self):
		return str(self.userID)

#PositiveSmallIntegerField(default=0)
