# -*- coding: utf-8 -*-
import scrapy
from chapagain.items import ChapagainItem


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']


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

        for href in response.css( "li.next a::attr(href)"):
            print('Next Page URL: ', href)
            yield response.follow(href, callback = self.parse)
   