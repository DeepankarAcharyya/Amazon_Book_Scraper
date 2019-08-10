# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbookscraperItem

class AmazonBookSpiderSpider(scrapy.Spider):
    name = 'amazon_book'

    start_urls = [
       'https://www.amazon.in/s?k=books+thriller+and+mystery&i=stripbooks&rh=n%3A976389031%2Cn%3A1318161031%2Cp_72%3A1318476031&dc&qid=1565464758&rnid=1318475031&ref=sr_nr_p_72_1',
    ]
    
    def parse(self, response):
        items=AmazonbookscraperItem()

        #selectors:
        #title:         .a-size-medium
        #author:        .a-spacing-none .a-color-secondary .a-size-base.a-link-normal
        #price:         .a-spacing-top-small .a-price:nth-child(1) .a-price-whole
        #image:         .a-spacing-none .s-image

        title =response.css(".a-size-medium").css("::text").extract()
        author=response.css(".a-spacing-none .a-color-secondary .a-size-base.a-link-normal").css('::text').extract().replace('\n',"").strip()
        price =response.css(".a-spacing-top-small .a-price:nth-child(1) .a-price-whole").css('::text').extract()
        image =response.css(".a-spacing-none .s-image").css('::attr(src)').extract()

        items['title']=title
        items['author']=author
        items['price']=price
        items['image_link']=image

        yield items