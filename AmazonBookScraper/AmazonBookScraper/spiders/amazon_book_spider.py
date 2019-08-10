# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbookscraperItem

class AmazonBookSpiderSpider(scrapy.Spider):
    name = 'amazon_book'

    start_urls = [
       'https://www.amazon.com/s?i=stripbooks&bbn=1000&rh=n%3A283155%2Cn%3A%211000%2Cn%3A18%2Cp_n_feature_nine_browse-bin%3A3291437011%2Cp_n_feature_browse-bin%3A2656022011%2Cp_n_condition-type%3A1294423011&dc&fst=as%3Aoff&qid=1565461357&rnid=1000&ref=sr_nr_n_20',
    ]
    

    def parse(self, response):
        items=AmazonbookscraperItem()

        title=response.css(".a-color-base.a-text-normal").extract()
        author=response.css(".a-color-secondary .a-size-base.a-link-normal").css('::text').extract()
        price=response.css(".a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole").css('::text').extract()
        image=response.css(".s-image-fixed-height").css('::attr(src)').extract()

        items['title']=title
        items['author']=author
        items['price']=price
        items['image_link']=image

        yield items