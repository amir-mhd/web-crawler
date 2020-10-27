import scrapy
from ..items import Hackernews_items


class Hackernews_crawler(scrapy.Spider):
    # assign a name to later call it in crawl command
    name = "hackernews"

    # determine which page should be the starting page
    start_urls = ["https://news.ycombinator.com/"]

    # settings for storing downloaded data
    custom_settings = {
        "FEED_FORMAT": "csv", "FEED_URI": "hackernews_data.csv"}

    # defining a method to parse the html and css in pages
    def parse(self, response):
        article_item = Hackernews_items() 
        articles_info = response.css("td.title")
        for article in articles_info:
            article_item["title"] = article.css("a::text").get()
            article_item["publisher"] = article.css("span.sitestr::text").get()
            yield article_item
    
        
        # get the next page link
        next_page = response.css("a.morelink::attr(href)").get()
        # check if there was an another page crawl that too
        if next_page is not None:
            for a in response.css("a.morelink"):
                # follow is just a shortcut of joinurl and it goes to the next relative URLs
                yield response.follow(a, callback=self.parse)
