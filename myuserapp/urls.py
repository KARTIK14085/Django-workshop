
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('home', views.homepage),
    path('about', views.about),
    path('contact', views.contact),
    path('shop', views.shop),
    path('savesessiondata', views.savesessiondata),
    path('getsessiondata', views.getsessiondata),
    path('delsessiondata', views.delsessiondata),
    path('savesessiondata2', views.savesessiondata2),
    path('login', views.login),
    path('loginprocess', views.loginprocess),
     path('dashboard', views.dashboard),
      path('logout', views.logout),
    
]