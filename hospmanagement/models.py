from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    skills=models.TextField()

    def __str__(self):
        return self.name

class appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=100)
    date=models.DateField()
    specialization=models.CharField(max_length=50)
    patient_email=models.EmailField(max_length=100)
    patient_phone=models.CharField(max_length=10)

class report(models.Model):
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    reportfile = models.FileField(upload_to='router_specifications')
    

class Vaccinations(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    def __str__(self):
        return self.name

class bookvac(models.Model):
    vaccinations=models.ForeignKey(Vaccinations,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=100)
    date=models.DateField()
    patient_email=models.EmailField(max_length=100)
    patient_phone=models.CharField(max_length=10)