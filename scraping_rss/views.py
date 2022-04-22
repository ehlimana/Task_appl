from django.shortcuts import render, redirect
from django.views import generic
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from scraping_rss.models import News
driver=webdriver.Chrome(ChromeDriverManager().install())
# Create your views here.
#takes request --->response
def rss_request(request):
    
    def get_queryset(self):
        return News.objects.all()
    return render (request,"rss_app.html")
#class HomePageView(generic.ListView):
    #template_name = 'home.html'
    #context_object_name = 'articles' 
    # assign "News" object list to the object "articles"
    # pass news objects as queryset for listview
    
        
