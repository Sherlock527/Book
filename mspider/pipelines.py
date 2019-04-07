# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy import Spider


class MspiderPipeline(object):
    def open_spider(self, spider:Spider):
        filename = spider.settings['filename']
        self.jsonfile = open(filename, 'w', encoding='utf-8')
        self.jsonfile.write('[\n')
        self.jsonfile.flush()

    def process_item(self, item, spider):
        self.jsonfile.write(json.dumps(dict(item)) + ',\n')
        return item

    def close_spider(self, spider:Spider):
        self.jsonfile.write(']')
        self.jsonfile.close()
