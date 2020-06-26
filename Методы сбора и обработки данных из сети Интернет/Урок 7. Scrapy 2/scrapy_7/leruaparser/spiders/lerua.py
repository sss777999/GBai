# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from leruaparser.items import LeruaparserItem
from scrapy.loader import ItemLoader


class LeruaSpider(scrapy.Spider):
    name = 'lerua'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}']

    def parse(self, response):
        ads_links = response.css('div.hover-image-buttons a::attr(href)').extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)

    def parse_ads(self, response: HtmlResponse):
        loader = ItemLoader(item=LeruaparserItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('price', '//span[@slot="price"]//text()')
        loader.add_xpath('characteristic', "//dl[@class='def-list']//text()")
        loader.add_xpath('photos', "//source[@media=' only screen and (min-width: 1024px)']/@data-origin")
        loader.add_value('link', response.url)
        yield loader.load_item()
