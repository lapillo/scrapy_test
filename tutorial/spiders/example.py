# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.ceneo.pl']
    start_urls = ['https://www.ceneo.pl/67951003']

    def parse(self, response):
        for quote in response.css('.cell-price'):
            yield {
                'text': quote.css('.value::text').get()
            } 