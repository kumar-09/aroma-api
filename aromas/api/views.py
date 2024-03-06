from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import userSerializer
from .serializers import menuSerializer
from main.models import menu
from .forms import menuaddform

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


@api_view(['POST'])
def addFood(request):
    form= menuaddform(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    return Response({'success': True, 'data': form.data})