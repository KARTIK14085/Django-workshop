
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('home', views.homepage),
    path('about', views.about),
    path('contact', views.contact),
    path('shop', views.shop),
    path('contactprocess', views.contactprocess),
    
]