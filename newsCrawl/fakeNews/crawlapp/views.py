from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import sys
sys.path.append('../newsCrawl/newsCrawl/spiders')

# sys.path.insert(0,'/home/arif/newsCrawl/newsCrawl/spiders')
from start import crawl



def crawling(request):
    return render(request,'crawling.html')

def crawlData(request):
    return 'project is under Development'
    
def testCrawling():
    crawl()




