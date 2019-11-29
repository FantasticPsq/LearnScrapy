# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse

from ..items import MyspiderItem


class WsbkSpider(scrapy.Spider):
    name = 'WSBK'
    allowed_domains = ['lovehhy.net']
    start_urls = ['http://www.lovehhy.net/Joke/Detail/QSBK/1']
    base_domains = "http://www.lovehhy.net"

    def parse(self, response):
        contents = response.xpath("//div[@id='footzoon']")
        titles = contents.xpath(".//h3//a//text()").extract()
        main_contents = contents.xpath(".//div[@id='endtext']//text()").extract()
        for i in range(0, len(titles)):
            title = "".join(titles[i]).strip()
            main_content = "".join(main_contents[i]).strip()
            item = MyspiderItem(title=title, content=main_content)
            yield item
        next_url = response.xpath("//div[@id='ct_page']//li[last()]/a/@href").get()
        print(next_url)
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domains + next_url, callback=self.parse)

