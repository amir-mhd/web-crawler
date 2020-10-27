from scrapy.item import Item, Field


class Hackernews_items(Item):
    title = Field()
    publisher = Field()

