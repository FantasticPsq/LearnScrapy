# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']  # 此处必须写正确，否则会出现filter to等错误
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r".+article-.+\.html"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        item = {}
        title = response.xpath("//h1[@class='ph']/text()").get()
        print(title)
        # return item
