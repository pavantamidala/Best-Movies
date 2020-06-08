from django.urls import path
from . import views

urlpatterns = [
    path('Tel/', views.Telugu, name='Te'),
    path('', views.English, name='in'),
    
   
]
