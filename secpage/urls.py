from django.urls import path
from secpage import views

urlpatterns = [
    path('', views.secpage, name='secpage'),
]