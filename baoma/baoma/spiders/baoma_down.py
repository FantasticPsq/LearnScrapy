# -*- coding: utf-8 -*-
import scrapy
from ..items import BaomaItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BaomaDownSpider(CrawlSpider):
    name = 'baoma_down'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/3941.html']

    rules = (
        Rule(LinkExtractor(allow=r"https://car.autohome.com.cn/pic/series/3941-.+"), callback='parse_page',
             follow=True),

    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']//div/text()").get()
        srcs = response.xpath("//div[contains(@class,'uibox-con')]/ul/li//img/@src").getall()
        images_url = list(map(lambda x: response.urljoin(x.replace("240x180_0_q95_c42_", "")), srcs))
        item = BaomaItem(category=category, image_urls=images_url)
        yield item
