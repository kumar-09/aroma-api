from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import userSerializer, loginSerializer

@api_view(['POST'])
def register(request):
    serializer = userSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data) 

@api_view(['GET'])
def login(request):

    permission_class = (IsAuthenticated, )
    serializer_class = userSerializer
    queryset = get_user_model().objets.all()
    
    serializer = loginSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
