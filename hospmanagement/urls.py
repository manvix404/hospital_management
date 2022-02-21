from django.urls import path
from. import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('appoint',views.appoint,name='appoint'),
    path('vaccine',views.vaccine,name='vaccine'),
    path('reports',views.reports,name='reports'),
    path('contact',views.contact,name='contact'),
    path('doctor',views.doctor,name='doctor'),
    path('services',views.services,name='services'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    ]