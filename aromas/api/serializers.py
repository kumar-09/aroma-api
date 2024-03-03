from rest_framework import serializers
from main.models import users


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = "__all__"