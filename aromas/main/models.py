from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class users(models.Model):
    userid = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=50)
    pswd = models.CharField(max_length=15)
    is_admin=models.BooleanField(default=False)
    mobile = models.IntegerField(validators=[MinValueValidator(6000000000),MaxValueValidator(9999999999)])
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.userid    

    class Meta:
        verbose_name_plural = 'users'

class category(models.Model):
    Type = models.CharField(primary_key=True,max_length=50)
    image = models.ImageField(upload_to='category/')    
    def __str__(self):
        return self.Type 
    class Meta:
        verbose_name='category items'
        verbose_name_plural = 'category'

class menu(models.Model):
    food_id = models.CharField(primary_key=True, max_length=50)
    Type=models.ForeignKey(category , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='food/')

    def __str__(self):
        return self.food_id
    
    class Meta:
        verbose_name_plural = 'menu'

class data(models.Model):
    userid = models.ForeignKey(users, on_delete=models.CASCADE,)
    cart_id = models.CharField(max_length=30)
    food_id = models.ForeignKey(menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(10)])
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.userid_id + '-' + self.cart_id

    class Meta:
        verbose_name_plural = 'data'


class session(models.Model):
    userid = models.ForeignKey(users, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=30)

    def __str__(self):
        return self.userid    

    class Meta:
        verbose_name_plural = 'session'    

