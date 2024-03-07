from rest_framework import serializers
from main.models import users
from main.models import menu,category


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('userid', 'name', 'pswd')

    def register(self, validated_data):
        #"""
        #Create and return a new `user` instance, given the validated data.
        #"""
        return users.objects.create(**validated_data)
    
class menuSerializer(serializers.ModelSerializer):

    # food_id = serializers.PrimaryKeyRelatedField()
    # name = serializers.CharField()
    # price = serializers.IntegerField()
    # image = serializers.ImageField()

    class Meta:
        model = menu
        fields = '__all__'

       
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields ='__all__'
