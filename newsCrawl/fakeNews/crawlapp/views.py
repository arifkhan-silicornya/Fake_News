from django.shortcuts import render
# Create your views here.

import sys
sys.path.append('../newsCrawl/newsCrawl/spiders')

sys.path.insert(0,'/home/arif/newsCrawl/newsCrawl/spiders')
from start import crawl


def crawling(request):
    return render(request,'crawling.html')

def crawlData(request):
    crawl()
    return render(request,'crawling.html')