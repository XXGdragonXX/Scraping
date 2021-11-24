#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy
from scrapy.crawler import CrawlerProcess
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
                
            }
            

process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()


# In[ ]:




