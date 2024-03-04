from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import menuSerializer
from main.models import menu
 

@api_view(['POST'])
def register(request):
    if request.Response == 'POST':
        return Response(request.data)
    
@api_view(['GET'])
def getmenu(request):
    Menulist = menu.objects.all()
    serializer = menuSerializer(Menulist , many=True)
    return Response(serializer.data)