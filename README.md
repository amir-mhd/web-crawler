# Project's Aim
This project was built to serve my personal need for learning how a crawler work? and how can I programm a crawler
For my own interests in tech news and cryptocurrency I chose to scrape [hackernews](https://news.ycombinator.com/) and [coinmarketcap](https://coinmarketcap.com/) 

# Technology
My crawler is written in **Scrapy**, Scrapy is an opensource *framework* and is written in **python**. It's one of the fastest webscraping/crawling frameworks out there (as far as I know!).
For more information about Scrapy project you can visit it's website [Here](https://scrapy.org/) 

# How It Works
My crawler will gather the title, publisher, and the article website link and save them in a csv file name "hackernews_data.csv" by default, you can change this default behavior by making changes in "custom_settings", for more information look at this [Doc](https://docs.scrapy.org/en/latest/topics/spiders.html?highlight=custom_setting#scrapy.spiders.Spider.custom_settings) in Scrapy official documentation 
Crawler is programmed to find the next page link in hackernews website, when it reaches the next page, it will crawl it and gather the same data in the new page and append it to the csv file 
