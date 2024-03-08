from django.urls import path,include
from . import views

urlpatterns = [
    path('menu/',views.getmenu, name='Menu'),
    path('register/',views.register),
    path('menu/<str:type>/',views.Category, name='Category'),
    path('addCart/',views.Cart, name='Cart'),
    path('category-list/',views.categorylist, name='Category list')
]

