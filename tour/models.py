from django.db import models

# Create your models here.
class webuser(models.Model):
    username = models.CharField(max_length=25,primary_key=True)
    password = models.CharField(default='000000',max_length=20)
    introduction = models.TextField()
    email = models.TextField()

class reviewlist(models.Model):
    reviewid = models.IntegerField(primary_key=True)
    attractionid=models.IntegerField()
    reviewuser= models.TextField()
    reviewcontent = models.TextField()

class attraction(models.Model):
    aid = models.IntegerField(primary_key=True)
    aname = models.TextField()
    tour = models.TextField()
    hotel = models.TextField()
    #reviews = models.ForeignKey(onereview,on_delete=models.CASCADE)