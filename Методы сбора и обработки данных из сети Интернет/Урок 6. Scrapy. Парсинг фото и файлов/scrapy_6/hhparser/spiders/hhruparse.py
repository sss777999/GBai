# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from hhparser.items import HhparserItem


class HhruparseSpider(scrapy.Spider):
    name = 'hhruparse'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://krasnogorsk.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=Artificial+intelligence&L_save_area=true&area=1&from=cluster_area&showClusters=true']


    def parse(self, response: HtmlResponse):
        next_page = response.css('a.HH-Pager-Controls-Next.HH-Pager-Control::attr(href)').extract_first()
        vacancy_links = response.css('div.vacancy-serp div.vacancy-serp-item a.HH-LinkModifier::attr(href)').extract()

        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)
        yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name_job = response.xpath('//h1/text()').extract_first()
        salary_job = response.css('p.vacancy-salary span::text').extract()
        yield HhparserItem(name=name_job, salary=salary_job, link=response.url)
