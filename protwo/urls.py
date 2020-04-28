from django.urls import path
from protwo import views

urlpatterns = [
    path('', views.protwo, name='protwo'),
]