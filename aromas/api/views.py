from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import userSerializer
from .serializers import menuSerializer , CategorySerializer,dataSerializer
from main.models import menu,category,users,data
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

@api_view(['GET'])
def Category(request , type):
    # itemlist=category.objects.filter(Type=type)    
    # serializer = CategorySerializer(itemlist , many=True)
    Menulist = menu.objects.filter(food_id__Type=type)
    serializer1 = menuSerializer(Menulist ,many=True)

    # data={
    #     # 'categories':serializer.data,
    #     'items':serializer1.data
    # }
    return Response(serializer1.data)

@api_view(['POST'])
def additem(request):
    serializer2=menuSerializer(data=request.data)

    if serializer2.is_valid():
        serializer2.save()
    return Response(serializer2.data)

@api_view(['GET'])
def PreviousOrders(request,pk):
    OrderUserid=data.objects.filter(userid=pk)
    serializer3=dataSerializer(OrderUserid , many=True)

    OrderList=data.objects.filter(userid=pk)
    # serializer4=
    return Response(serializer3.data)


