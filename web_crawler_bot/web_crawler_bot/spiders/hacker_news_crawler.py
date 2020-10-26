import scrapy

class Crawler(scrapy.Spider):
    name = "hackernews"

    start_urls = ["https://news.ycombinator.com/"]


    def parse(self, response):
        titles = response.css("td.title a")
        for title in titles:
            yield{
                "title": title.css("a::text").getall()
            }         

