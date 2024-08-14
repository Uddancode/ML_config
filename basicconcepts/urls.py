from django.urls import include, path
from . import views

urlpatterns=[
     path('',views.Welcome, name='Welcome'), 
    
    path('user',views.User,name='User'),
]