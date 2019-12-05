# -*- coding: utf-8 -*-
import scrapy


def parse_after_login(response):
    print(response.url)
    if response.url == "https://www.douban.com/":
        print("登陆成功")
    else:
        print("登陆失败")


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']
    login_url = 'https://accounts.douban.com/passport/login'  # 注意这个url后面不能加/

    def parse(self, response):
        formdata = {
            'ck': '',
            'name': '1636538091@qq.com',
            'password': 'psq1587473',
            'remember': 'true',
            'ticket': ''
        }
        yield scrapy.FormRequest(url=self.login_url, formdata=formdata, callback=parse_after_login,dont_filter=True)
