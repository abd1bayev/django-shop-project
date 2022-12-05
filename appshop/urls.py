from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index, name='index'),
    
    path('cart/', cart),
    path('checkout/', checkout),
    path('contact/', contact),
    path('detail/', detail),
    path('shop/', shop),
    
]
