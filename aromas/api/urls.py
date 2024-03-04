from django.urls import path,include
from . import views

urlpatterns = [
    path('menu/',views.getmenu, name='Menu'),
    path('register/',views.register),
]

