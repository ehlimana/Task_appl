from django.contrib import admin
from django.urls import path,include
from . import views
#from .views import HomePageView
urlpatterns=[
   path("sel/",views.rss_request),
    #path('', HomePageView.as_view(), name='home')
]