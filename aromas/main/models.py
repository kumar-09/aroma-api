from django.db import models

# Create your models here.

class menu(models.Model):
    food_id = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    image=models.ImageField(upload_to='images/')
    price= models.IntegerField()
 
    def __str__(self):
        return self.name
