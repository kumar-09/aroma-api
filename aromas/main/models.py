from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class users(models.Model):
    userid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=50)
    pswd = models.CharField(max_length=15)
class menu(models.Model):
    food_id = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/')

class data(models.Model):
    userid = models.ForeignKey(users, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=30)
    food_id = models.CharField(max_length=50)
    quantity = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
