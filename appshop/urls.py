from django.urls import path
from .views import *


urlpatterns = [
    path('index', index, name='index'),
    
    path('error', error),
    path('about', about),
    path('address', address),
    path('alerts', alerts),
    
]