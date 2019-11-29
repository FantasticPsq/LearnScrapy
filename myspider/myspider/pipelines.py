# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter
from scrapy.exporters import JsonLinesItemExporter


class MyspiderPipeline(object):
    def __init__(self):
        self.fp = open("duanzi.josn", "wb")  # 使用JsonItemExporter或者JsonLinesItemExporter需要以二进制方式打开文件
        # 使用JsonLinesItemExporter好处是结果一行一行展示，便于观察，而且不耗费内存，数据直接与硬盘打交道而比较安全，坏处是结果不符合Json规则
        # 使用JsonItemExporter好处是结果符合Json规则，但是不便于观察，且比较耗费内存
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        print("爬虫开始")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        print("爬虫结束")
