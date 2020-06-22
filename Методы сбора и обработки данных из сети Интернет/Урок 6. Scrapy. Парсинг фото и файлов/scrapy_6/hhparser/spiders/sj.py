# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from hhparser.items import HhparserItem


class SjSpider(scrapy.Spider):
    name = 'sj'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://russia.superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response):
        next_page = response.css('a.f-test-link-Dalshe::attr(href)').extract_first()
        vacancy_links = response.css('div._3mfro.PlM3e._2JVkc._3LJqf a.icMQ_._6AfZ9::attr(href)').extract()

        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)
        yield response.follow(next_page, callback=self.parse)

    def vacancy_parse(self, response: HtmlResponse):
        name_job = response.xpath('//h1/text()').extract_first()
        # salary_job = response.xpath('//span[contains(@class, "_1OuF_ ZON4b")]').extract()
        salary_job = response.css('span._1OuF_.ZON4b span._3mfro._2Wp8I.PlM3e._2JVkc::text').extract()
        # salary_job = ''.join(salary_job)
        yield HhparserItem(name=name_job, salary=salary_job, link=response.url)
