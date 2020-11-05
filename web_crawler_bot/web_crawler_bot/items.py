from scrapy.item import Item, Field


class Hackernews_items(Item):
    title = Field()
    publisher = Field()
    article_link = Field()

class Coinmarketcap_items(Item):
    cryptocurrenci = Field()
    price = Field()
    market_cap = Field()
    change_percent_in_24h = Field()