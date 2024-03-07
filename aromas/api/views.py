from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import userSerializer
from .serializers import menuSerializer , CategorySerializer
from main.models import menu,category
 

@api_view(['POST'])
def register(request):
    serializer = userSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
    if request.Response == 'POST':
        return Response(request.data)
    
@api_view(['GET'])
def getmenu(request):
    Menulist = menu.objects.all()
    serializer = menuSerializer(Menulist , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Category(request , pk):
    Menulist=category.objects.get(food_id=pk)    
    serializer = CategorySerializer(Menulist , many=False)
    return Response(serializer.data)