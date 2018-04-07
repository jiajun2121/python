# -*- coding: utf-8 -*-
import scrapy
import json


class DyttspiderSpider(scrapy.Spider):
    name = 'dyttspider'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/']

    def parse(self, response):
        for href in response.xpath('.//tr/td[1]/a[2]'):
            full_url = response.urljoin(
                href.re('''href="(.*?)">(?:.*?)</a>''')[0])
            with open(r'url.txt', 'a+', encoding='utf-8') as fp:
                fp.write(full_url + '\n')
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        info = {'magnet': response.xpath('.//tbody/tr/td/a').extract()[0],
                'title': response.xpath('.//*[@id="header"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/h1/font').extract()[0],
                }
        with open(r'info.json', 'a+', encoding='utf-8') as fp:
            fp.write(json.dumps(info) + '\n')
        yield info
