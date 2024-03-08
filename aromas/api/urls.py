from django.urls import path,include
from . import views

urlpatterns = [
    path('menu/',views.getmenu, name='Menu'),
    path('register/',views.register),
    path('additem/',views.addFood),
    path('menu/<str:type>/',views.Category, name='Category'),
    path('additem/',views.additem,name='NEWITEM'),
    path('prevlist/<str:pk>',views.PreviousOrders,name='LastOrders')
]

