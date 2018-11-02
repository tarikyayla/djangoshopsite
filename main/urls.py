from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('katalog/',views.katalog),
    path("katalog/<int:id>",views.katalog),
    path("urundetay/<int:id>",views.urundetay),
    path("register/",views.register),
    path("login/",views.user_login),
    path('logout/',views.user_logout),
    path('search/<str:searchtext>',views.search),
    path("cart/",views.cart)
]