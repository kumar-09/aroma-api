from rest_framework import serializers
from main.models import users
from main.models import menu,category,data,data
from django.contrib.auth import get_user_model


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

    def register(self, validated_data):
        return users.objects.create(**validated_data)
    
class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'
       
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields ='__all__'

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=data
        fields=['cart_id']

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['userid', 'pswd']

class ordertestSerializer(serializers.ModelSerializer):
    class Meta:
        model=data
        fields=['food_id','quantity']

        
    