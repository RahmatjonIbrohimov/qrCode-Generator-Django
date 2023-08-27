from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wifi/', views.wifi, name='wifi-qrcode'),
    path('link/', views.link, name='link-qrcode'),
    path('telegram/', views.telegram, name='telegram-qrcode'),
    path('instagram/', views.instagram, name='instagram-qrcode'),
    path('twitter/', views.twitter, name='twitter-qrcode'),
    path('facebook/', views.facebook, name='facebook-qrcode'),
]
