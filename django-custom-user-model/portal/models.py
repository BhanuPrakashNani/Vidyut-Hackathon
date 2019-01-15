from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=15)
    service = models.CharField(max_length=150)
    date = models.DateField("Date", default=date.today)
    token_no = models.IntegerField()

    def __str__(self):
        return self.name

class Cod(models.Model):
    roll_no = models.CharField(max_length=75)
    service=models.CharField(max_length=150)
    Eta=models.DateField("Date", default=date.today)
    tracking_id = models.CharField(max_length=30)
    payment = models.IntegerField()


    def __str__(self):
        return self.roll_no

