from django.urls import path
from mywebpage import views

urlpatterns = [
    path('', views.mywebpage, name='mywebpage'),
]