# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem


class Book24parserSpider(scrapy.Spider):
    name = 'book24parser'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/knigi-bestsellery/']

    def parse(self, response: HtmlResponse):
        next_page = ''.join(
            response.css('a.catalog-pagination__item._text.js-pagination-catalog-item::attr(href)').extract())
        # 2 одинаковых класса, первый мешал
        if '//' in next_page:
            next_page = ''.join(
                response.css('a.catalog-pagination__item._text.js-pagination-catalog-item::attr(href)').extract()[1])
        vacancy_links = response.css(
            'div.catalog-products__list.js-catalog-products  a.book__image-link.js-item-element.ddl_product_link::attr(href)').extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)
        yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name_book = response.xpath("//h1/text()").extract_first()
        # помню, что тут чисто апарсинг, но тут сам запрос разный от условия, мне так удобнее показалось
        author_book = response.css('div.item-tab__chars-list span::text').extract()
        if author_book[0] == 'Автор: ' or author_book[0] == 'Автор:':
            author_book = response.css('div.item-tab__chars-list a.item-tab__chars-link::text').extract_first()
        else:
            author_book = 'Автор не указан'
        # price_book = response.xpath('//div[contains(@class, "item-actions__prices")]//text()').extract()
        price_book = [response.css('div.item-actions__buttons-box div.item-actions__price b::text').extract_first()]
        newprice_book = response.css('div.item-actions__buttons-box div.item-actions__price-old::text').extract_first()
        if newprice_book:
            price_book.append(newprice_book)
        rate_book = response.xpath('//span[@class="rating__rate-value"]/text()').extract()
        rate_book = ''.join(rate_book)
        yield BooksparserItem(link=response.url, name=name_book, author=author_book, price=price_book,
                              rate=rate_book)
