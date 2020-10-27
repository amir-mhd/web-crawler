import scrapy

class Crawler(scrapy.Spider):
    name = "hackernews"

    start_urls = ["https://news.ycombinator.com/",
                  "https://news.ycombinator.com/news?p=2",
                   "https://news.ycombinator.com/news?p=3"
    ]


    def parse(self, response):
        titles = response.css("td.title a")
        for title in titles:
            yield{
                "title": title.css("a::text").get(),
                "publisher": title.css("span.sitestr::text").get()
            }         

        next_page = response.css("a.morelink::attr(href)").get()
        
        if next_page is not None:
            for a in response.css("a.morelink::attr(href)"):
                yield response.follow(a, callback=self.parse)
            
