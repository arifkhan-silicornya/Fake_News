import scrapy


class NewSpider(scrapy.Spider):
    name="fakenews"

    start_urls = [
        'https://www.prothomalo.com'
    ]

    def parse(self, response):

        for title in response.css('.story-element div '):
            yield {
                'title': title.css('p::text').getall()
            }
        
        next_page = response.css('.home-m__collection-container__3Isby a::attr(href)').getall()
        if next_page is not None:
            for data in next_page:
                data = response.urljoin(data)
                yield scrapy.Request(data, callback=self.parse)
        

# crapy crawl fakenews -o save.csv.split()