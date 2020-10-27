import scrapy

class Crawler(scrapy.Spider):
    # assign a name to later call it in crawl command
    name = "hackernews"

    # determine which page should be the starting page
    start_urls = ["https://news.ycombinator.com/"]

    # defining a method to parse the html and css in pages
    def parse(self, response):
        titles = response.css("td.title a")
        for title in titles:
            yield{
                "title": title.css("a::text").get(),
                "publisher": title.css("span.sitestr::text").get()
            }         

        # get the next page link
        next_page = response.css("a.morelink::attr(href)").get()
        # check if there was another page crawl that too
        if next_page is not None:
            for a in response.css("a.morelink"):
                # follow just is a shortcut to go to next relative URLs
                yield response.follow(a, callback=self.parse)
            
