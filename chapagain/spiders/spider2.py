# -*- coding: utf-8 -*-
import scrapy
from chapagain.items import ChapagainItem
import shup
shub.login
API key: e526b7cd9e8d4244a1d31f4b3b9ed29a
shub deploy 474604


class Spider1Spider(scrapy.Spider):
    name = 'spider2'
    
    allowed_domains = ['quotes.toscrape.com']

    start_urls = ['http://quotes.toscrape.com/page/%s' % page for page in range(1, 7)]


    def parse(self, response):
        print("Response Type >>>" , type(response))
        rows = response.css("div.quote")  # root element
        for row in rows:
            item = ChapagainItem()
            item[ 'tags' ] = row.css('div.tags > meta[itemprop="keywords"]::attr\
("content")').extract_first()
            item[ 'author' ] = row.css('small[itemprop="author"]::text').extract_first()
            item[ 'quote' ] = row.css('span[itemprop="text"]::text').extract_first()
            item[ 'author_link' ] = row.css('a:contains("(about)")::attr(href)').extract_first()
            if len(item[ 'author_link' ])>0:
                item[ 'author_link' ] = 'http://quotes.toscrape.com' +item[ 'author_link']
            yield item 