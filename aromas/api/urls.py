from django.urls import path,include
from . import views

urlpatterns = [
    path('menu/',views.getmenu, name='Menu'),
    path('register/',views.register),
    path('login/',views.login, name='Login'),
    path('menu/<str:type>/',views.menu_category, name='Category'),
    path('additem/',views.additem,name='NEWITEM'),
    path('prevlist/<str:pk>',views.PreviousOrders,name='LastOrders'),
    path('addCart/',views.addCart, name='Cart'),
    path('all-category-menu/',views.all_category_menu, name='Category list'),
    path('category-list/',views.categorylist, name='Category list'),
]

