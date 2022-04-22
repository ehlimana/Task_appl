
from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import app, shared_task
from .models import News
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import json
from datetime import datetime
import lxml

# logging
#from celery.utils.log import get_task_logger

#logger = get_task_logger(__name__)



def get_url(driver,url):
    driver.get(url)
    return driver
@shared_task
def fetch_and_scrape(request):
    article_list=[]
    options=Options()
    options.headless=True
    options.add_argument("--window-size=1920,1080")
    driver=webdriver.Chrome(options=options)
    next1 = driver.find_elements_by_tag_name('item')

    for a in next1 :
        print('Starting the scraping tool')
        title = a.find_element_by_tag_name ("title")
        title=title.get_attribute("textContent")
            
        description = a.find_element_by_xpath ('description')
        description=description.get_attribute("textContent")
        
        link = a.find_element_by_tag_name ("link")
        link=link.get_attribute("textContent")
            
        published = a.find_element_by_xpath ('pubDate')
        published=published.get_attribute("textContent")
        
        article = {
                    'title': title,
                    'description': link,
                    'link': link,
                    'published': published  }
    
        article_list.append(article)
        print('Finished scraping the articles')
         # after the loop, dump my saved objects into a .txt file
        return save_function(article_list)
    
                # after the loop, dump my saved objects into a .txt file

@shared_task(serializer='json')
def save_function(article_list):
    print('starting')
    new_count = 0

    for article in article_list:
        try:
            News.objects.create(
                title = article['title'],
                link = article['link'],
                published = article['published'],
                description = article['description']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')