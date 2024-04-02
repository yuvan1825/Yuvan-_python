from django.urls import include, path
from appyuvan import views
urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('cart/',views.cart),
    path('login/',views.user_login),
    path('register/',views.register),
]
