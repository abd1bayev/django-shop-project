from django.urls import path
from .views import *


urlpatterns = [
    path('index', index, name='index'),
    
    path('error', error),
    path('about', about),
    path('address', address),
    path('alerts', alerts),
    path('blog_full', blog_full),
    path('blog_grid', blog_grid),
    path('blog_left', blog_left),
    path('blog_right', blog_right),
    path('blog_single', blog_single),
    path('buttons', buttons),
    path('cart/', cart),
    path('checkout', checkout),
    path('coming_soon', coming_soon),
    path('confirmation', confirmation),
    path('contact', contact),
    path('dashboard', dashboard),
    path('empty_cart', empty_cart),
    path('faq', faq),
    path('forget_password', forget_password),
    path('login', login),
    path('order', order),
    path('pricing', pricing),
    path('product_single', product_single),
    path('profile_details', profile_details),
    path('purchase_confirmation', purchase_confirmation),
    path('shop_sidebar', shop_sidebar),
    path('shop', shop),
    path('signin', signin),
    path('typography', typography),
    
    
]