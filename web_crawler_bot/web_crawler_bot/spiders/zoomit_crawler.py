import scrapy

class Crawler(scrapy.Spider):
    name = "zoomit"

    start_urls = ["https://www.zoomit.ir/"]

    def parse(self, response):
        posts = response.css("div.row")
        for post in posts:
            yield {
                "title": post.css("a.Home__LatestTopic_Title::text") 
            }