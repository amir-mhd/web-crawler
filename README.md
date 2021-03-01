This is a crawler written in "Scrapy" framework, Scrapy is opensource project, It's written in python and is one of the fastest webscraping/crawling framework out there.

You can use Scrapy to achieve different purposes like gathering data from acrros the web for data science project, downloading data for your personal work or ... .

For more information about Scrapy project you can visit it's website at:
--  https://scrapy.org/  -- 

This specific webcralwer is synced for crawler the hacker news website, hackernews website is a place which different people around the world gather around and share thier favorite articles with each other.

This crawler will get the title, publisher, and the article website link and save them in a csv file name "hackernews_data.csv" by default, you can change this default behavior by making changes in "custom_settings", for more information look at this link in Scrapy official documentation https://docs.scrapy.org/en/latest/topics/spiders.html?highlight=custom_setting#scrapy.spiders.Spider.custom_settings

Crawler is written to find the next page link, when it reaches the next page it will crawl the page and find the same data in the new page and store it in the same csv file 
