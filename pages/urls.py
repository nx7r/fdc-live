from turtle import home
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('home/', views.homePage,),
    path('events/', views.eventsPage, name='events'),
]