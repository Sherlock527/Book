# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response.html import HtmlResponse
from ..items import BookItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=False),
    )

    custom_settings = {'filename': 'book.json'}

    def parse_item(self, response: HtmlResponse):
        print(0, response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

        # i = 1
        for subject in response.xpath('//li[@class="subject-item"]'):
            item = BookItem()

            title = subject.xpath('.//h2/a//text()').extract()
            item['title'] = ''.join(map(lambda x: x.strip(), title))  # 合并副标题

            rate = subject.xpath('.//span[@class="rating_nums"]/text()').extract()
            item['rate'] = rate[0] if rate else '0'  # 有可能没有评分

            # print(i, response.url)
            # print(i, dict(item))
            # i += 1

            yield item