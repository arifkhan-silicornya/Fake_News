import os

def crawl():
    cmd = 'scrapy crawl fakenews -o output.csv --nolog'
    os.system(cmd)