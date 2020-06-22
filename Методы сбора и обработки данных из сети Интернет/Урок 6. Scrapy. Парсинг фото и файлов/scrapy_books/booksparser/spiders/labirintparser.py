# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem


class LabirintparserSpider(scrapy.Spider):
    name = 'labirintparser'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/rating/?period=2&id_genre=-1&nrd=1']

    def parse(self, response: HtmlResponse):
        next_page = response.css('div.pagination-next a::attr(href)').extract_first()
        vacancy_links = response.css('div.products-row  a.cover::attr(href)').extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)
        yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name_book = response.xpath("//h1/text()").extract_first()
        # помню, что тут чисто парсинг, но тут сам запрос разный от условия, мне так удобнее показалось
        # в каждом пауке нюанс по price, поэтому к единому виду приводим его перед попаданием в pipelines
        author_book = response.css('div.authors::text').extract()
        if author_book[0] == 'Автор: ':
            author_book = response.css('div.authors a::text').extract_first()
        else:
            author_book = 'Автор не указан'
        price_book = [response.css('div.buying span::text').extract()]
        price_book = [response.css('div.buying span::text').extract()[1]]
        newprice_book = response.css('div.buying span::text').extract()[0]
        if newprice_book.isdigit():
            price_book.append(newprice_book)
        rate_book = response.xpath('//div[@id="rate"]/text()').extract()
        rate_book = ''.join(rate_book)
        yield BooksparserItem(link=response.url, name=name_book, author=author_book, price=price_book, rate=rate_book)
