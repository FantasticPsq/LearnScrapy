# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse

from ..items import MyspiderItem


class WsbkSpider(scrapy.Spider):
    name = 'WSBK'
    allowed_domains = ['lovehhy.net']
    start_urls = ['http://www.lovehhy.net/Joke/Detail/QSBK/1']

    def parse(self, response):
        contents = response.xpath("//div[@id='footzoon']")
        titles = contents.xpath(".//h3//a//text()").extract()
        main_contents = contents.xpath(".//div[@id='endtext']//text()").extract()
        next_url = "http://www.lovehhy.net/" + "".join(response.xpath("//div[@id='ct_page']/li/first()").get())
        print(next_url)
        for i in range(0, len(titles)):
            title = "".join(titles[i]).strip()
            main_content = "".join(main_contents[i]).strip()
            item = MyspiderItem(title=title, content=main_content)
            yield item
