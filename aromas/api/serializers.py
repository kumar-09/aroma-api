from rest_framework import serializers
from main.models import users
from django.contrib.auth import get_user_model


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = "__all__"

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['userid', 'pswd']
    