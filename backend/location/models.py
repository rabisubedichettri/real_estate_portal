from django.db import models
from .choices import SubDistrict_CHOICES

class Provience(models.Model):
    name = models.CharField(max_length=15,unique=True)
    description = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name



class District(models.Model):
    name = models.CharField(max_length=15,unique=True)
    description = models.CharField(max_length=100,blank=True)
    provience = models.ForeignKey(Provience, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubDistrict(models.Model):
    name=models.CharField(max_length=15,unique=True)
    type=models.CharField(max_length=25,choices=SubDistrict_CHOICES)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class Ward(models.Model):
    name=models.CharField(max_length=20,unique=True)
    subdistrict=models.ForeignKey(SubDistrict,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return  self.name

