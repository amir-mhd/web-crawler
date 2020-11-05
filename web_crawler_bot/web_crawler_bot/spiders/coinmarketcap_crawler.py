import scrapy
from ..items import Coinmarketcap_items

class Coinmarketcap_crawler(scrapy.Spider):
    name = "coinmarketcap"

    start_urls = ["https://coinmarketcap.com/"]

    custom_settings = {
    "FEED_FORMAT": "csv", "FEED_URI": "coinmarketcap_data.csv"}

    def parse(self, response):
        item = Coinmarketcap_items()
        whole_chart = response.css("tbody").get()
        for every_part in whole_chart:
            item["cryptocurrenci"] = every_part.response.css("tbody > tr > td > a > div > div > p::text").getall()
            