from scrapy import cmdline


def crawl():
    cmdline.execute("scrapy crawl fakenews -o output.csv".split())

# crawl()