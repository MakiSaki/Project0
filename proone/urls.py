from django.urls import path
from proone import views

urlpatterns = [
    path('', views.proone, name='proone'),
]