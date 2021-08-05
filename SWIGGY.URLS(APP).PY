from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='swiggy'),
    path('login',views.login,name='swiggy'),
    path('order',views.order,name='swiggy'),
]