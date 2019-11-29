# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import WxappItem


class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']  # 此处必须写正确，否则会出现filter to等错误
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r".+article-.+\.html"), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        authors = response.xpath("//p[@class='authors']")
        author = authors.xpath("./a/text()").get()
        pub_time = authors.xpath("./span/text()").get()
        content = response.xpath("//td[@id='article_content']//p//text()").getall()
        content = "".join(content).strip()
        # print('title:%s' % title, 'author:%s' % author, 'pub_time:%s' % pub_time, "content:%s" % content)
        item = WxappItem(title=title, author=author, pub_time=pub_time, content=content)
        yield item
