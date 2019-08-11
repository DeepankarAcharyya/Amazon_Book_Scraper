# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonbookscraperItem

class AmazonBookSpiderSpider(scrapy.Spider):
    name = 'amazon_book'

    start_urls = [
        'https://www.amazon.in/gp/bestsellers/books/1318157031?ref_=Oct_BSellerC_1318157031_SAll&pf_rd_p=1ff43274-d0d9-5cbc-98d7-49245af7bfd9&pf_rd_s=merchandised-search-10&pf_rd_t=101&pf_rd_i=1318157031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=D67SKYFJDTMGPK851KSS&pf_rd_r=D67SKYFJDTMGPK851KSS&pf_rd_p=1ff43274-d0d9-5cbc-98d7-49245af7bfd9'   
    ]
    
    def parse(self, response):
        items=AmazonbookscraperItem()

        title =response.css("div.p13n-sc-truncated").css("::attr(title)").extract()
        author=response.css(".a-link-child").css('::text').extract()
        image =response.css("img").css('::attr(src)').extract()

        items['title']=title
        items['author']=author
        items['image_link']=image

        yield items