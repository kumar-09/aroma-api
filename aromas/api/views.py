from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import userSerializer, loginSerializer
from .serializers import menuSerializer , CategorySerializer
from main.models import menu,category,data
from django.http import HttpResponse,JsonResponse
import json

@api_view(['POST'])
def register(request):
    serializer = userSerializer(data=request.data)
    
    d = {
        'userid':request.data['userid'],
        'name':request.data.get('name')
    }
    if serializer.is_valid():
        serializer.save()
        return HttpResponse(json.dumps(d),"Sucessfully created user.", status = 201)
    return HttpResponse(json.dumps(d),"User already exists.", status = 400)
    # return Response(serializer.data)
    
@api_view(['GET'])
def getmenu(request):
    Menulist = menu.objects.all()
    serializer = menuSerializer(Menulist , many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Category(request , type):
    Menulist = menu.objects.filter(food_id__Type=type)
    serializer1 = menuSerializer(Menulist ,many=True)

    return Response(serializer1.data)

@api_view(['POST'])
def Cart(request):
    user = (request.data).get('userid')
    cart = (request.data).get('cart_id')
    foodid = (request.data).get('food_ids')
    quant = (request.data).get('quantity')
    for i in range(len(foodid)):
        data.objects.create(userid_id = user, cart_id = cart, food_id_id = foodid[i], quantity = quant[i])
    return HttpResponse("cart added", status = 201) 

@api_view(['GET'])
def categorylist(request, type):    
    cat = category.objects.all()
    catlist = list()
    typelist = list()
    #for i in range(len(cat)):


@api_view(['GET'])
def login(request):

    permission_class = (IsAuthenticated, )
    serializer_class = userSerializer
    queryset = get_user_model().objets.all()
    
    serializer = loginSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
