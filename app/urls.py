from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name='home'),
    path('createCourse/',createCourse,name='createCourse'),
    path('description/<str:pk>',description,name='description'),
    path('deleteCourse/<str:pk>/',deleteCourse,name='deleteCourse'),
    path('register/', registerPage,name='register'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
]
