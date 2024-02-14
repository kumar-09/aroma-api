from django.db import models

# Create your models here.

class users(models.Model):
    userid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=50)
    pswd = models.CharField(max_length=15)

class data(models.Model):
    userid = models.ForeignKey(users, on_delete=models.CASCADE)
    food_id = models.CharField(max_length=50)