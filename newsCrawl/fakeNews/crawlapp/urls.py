from django.urls import path
# from django.urls import include
from . import views

urlpatterns = [
    path('',views.crawling,name='actionCrawler'),
    path('',views.crawlData,name='crawlNews')
]
