from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login, name='Login'),
    path('addCart/',views.addCart, name='Cart'),
    path('category-list/',views.categorylist, name='Category list'),
    path('all-category-menu/',views.all_category_menu, name='Category list'),
    path('menu/',views.getmenu, name='Menu'),
    path('menu/<str:type>/',views.menu_category, name='Category'),
    path('additem/',views.additem,name='NEWITEM'),
    path('prevlist/<str:pk>',views.PreviousOrders,name='LastOrders'),
    path('logout/<str:userid>/<str:session_key>/', views.logout, name='Logout'),
    
    path('is-authenticated/<str:session_key>/',views.isauth, name='User Authentication'),
]

