# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['ipip.net']
    start_urls = ['http://myip.ipip.net/']

    def parse(self, response):
        print('test ip:', response.text)
        return response.text
