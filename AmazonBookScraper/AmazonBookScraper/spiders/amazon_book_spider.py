# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbookscraperItem

class AmazonBookSpiderSpider(scrapy.Spider):
    name = 'amazon_book'

    start_urls = [
       'https://www.amazon.in/s?i=stripbooks&bbn=1318161031&rh=n%3A976389031%2Cn%3A976390031%2Cn%3A1318161031%2Cp_n_binding_browse-bin%3A1318376031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_availability%3A1318484031%2Cp_n_condition-type%3A8609960031%2Cp_n_publication_date%3A2684819031&dc&fst=as%3Aoff&qid=1565468209&rnid=2684818031&ref=sr_nr_p_n_publication_date_1',
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