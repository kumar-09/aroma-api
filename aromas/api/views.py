from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import userSerializer, menuSerializer , CategorySerializer,dataSerializer,ordertestSerializer
from main.models import menu,category,users,data
from django.http import HttpResponse
import json
# from django.contrib.auth import get_user_model

@api_view(['POST'])
def register(request):

    #return request
    serializer = userSerializer(data=request.data)
    
    d = {
        'userid':request.data.get('userid'),
        'name':request.data.get('name'),
    }
    if serializer.is_valid():
        serializer.save()
        return HttpResponse(json.dumps(d),status = 201)
    return HttpResponse("User Already Exist",status = 400)
    
@api_view(['GET'])
def getmenu(request):
    Menulist = menu.objects.all()
    serializer = menuSerializer(Menulist , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def menu_category(request , type):
    Menulist = menu.objects.filter(Type=type)
    serializer = menuSerializer(Menulist ,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def additem(request):
    food_data={
        'food_id' : request.data.get('food_id'),
        'Type' : request.data.get('Type'),
        'name' : request.data.get('name'),
        'price' : request.data.get('price'),
        'image' : request.data.get('image'),
    }
    cat_Data={
        'Type': request.data.get('Type'),
        'image' : request.data.get('cat_image'),
    }
    serialisedCategory = CategorySerializer(data=cat_Data)
    if serialisedCategory.is_valid():
        serialisedCategory.save()
        serialisedFood = menuSerializer(data=food_data)
        if serialisedFood.is_valid():
            serialisedFood.save()
            return Response({'message':'Item added Successfully'}, status=200)
        else:
            return Response({'err':'Item Already Exist'}, status=400)
    else:
        serialisedFood = menuSerializer(data=food_data)
        if serialisedFood.is_valid():
            serialisedFood.save()
            return Response({'message':'Item added Successfully'}, status=200)
        else:
            return Response({'err':'Item Already Exist'}, status=400)


@api_view(['GET'])
def PreviousOrders(request,pk):
    PrevOrderList=[]
    OrderUserid=data.objects.filter(userid=pk)
    serializer1=dataSerializer(OrderUserid , many=True)
    OrderList=data.objects.filter(userid=pk)
    serializer2=ordertestSerializer(OrderList ,many=True)
    for OrderCartId in serializer1.data:
        Cartid=OrderCartId['cart_id']
        dict2=[]    
        for OrderData in serializer2.data:
            if OrderData['cart_id']==Cartid:
                FoodId=OrderData['food_id']
                Quantity=OrderData['quantity']
                dict2.append({FoodId:Quantity})
        PrevOrderList.append({Cartid:dict2})
    return Response(PrevOrderList)

@api_view(['POST'])             
def addCart(request):
    user = (request.data).get('userid')
    cart = (request.data).get('cart_id')
    foodid = (request.data).get('food_ids')
    quant = (request.data).get('quantity')
    for i in range(len(foodid)):
        data.objects.create(userid_id = user, cart_id = cart, food_id_id = foodid[i], quantity = quant[i])
    return HttpResponse("cart added", status = 201) 

@api_view(['GET'])
def all_category_menu(request):    
    menulist = menu.objects.all()
    serializer = menuSerializer(menulist, many = True)
    catdict = dict()

    for data in serializer.data:
        if [data,] != catdict.setdefault(data['Type'], [data,]):
            catdict[data['Type']].append(data)
    
    return Response(catdict)


@api_view(['POST'])
def login(request):
    userlist = list(users.objects.all().values())
    data = request.data
    p1 = data.get('userid')
    p2 = data.get('pswd')
    d = {
        'userid': p1,
        'pswd': p2
    }
    for user in userlist:
        if user.get('userid') == d['userid'] and user.get('pswd') == d['pswd']:
            dic={
                'userid':user.get('userid'),
                'name':user.get('name'),
            }
            return HttpResponse(json.dumps(dic), status=200)
    return HttpResponse(json.dumps({'message': 'Invalid credentials'}), status=400)

@api_view(['GET'])
def categorylist(request):
    catlist = category.objects.all()
    serializer = CategorySerializer(catlist, many = True)
    return Response(serializer.data)

