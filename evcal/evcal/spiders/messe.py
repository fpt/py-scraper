# -*- coding: utf-8 -*-
import scrapy

import sys
import codecs
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

class MesseSpider(scrapy.Spider):
    name = "messe"
    allowed_domains = ["m-messe.co.jp"]
    start_urls = (
        'http://www.m-messe.co.jp/event/list',
    )

    def parse(self, response):
        for sel in response.xpath('//ul[@class="event_list"]/li[contains(@class, "Event")]'):
            id = sel.xpath('p[@class="event_head"]/a/@id').extract()
            title = sel.xpath('p[@class="event_head"]/a/text()').extract()
            date = sel.xpath('div[@class="event_body"]//tr[1]/td[@class="right"]/text()').extract()
            time = sel.xpath('div[@class="event_body"]//tr[2]/td[@class="right"]/text()').extract()
            desc = sel.xpath('div[@class="event_body"]//tr[3]/td[@class="right"]/text()').extract()
            fee  = sel.xpath('div[@class="event_body"]//tr[4]/td[@class="right"]/text()').extract()
            link = sel.xpath('div[@class="event_body"]//tr[8]/td[@class="right"]/text()').extract()
            id = id[0].strip()
            title = title[0].strip()
            date = date[0].strip()
            time = time[0].strip()
            desc = desc[0].strip()
            fee = fee[0].strip()
            print "--------------------------------"
            print id, title, date, time, desc, fee, link

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//p[@class="event_head"]/a/@id').re(r'(\d+)')
        item['name'] = response.xpath('//p[@class="event_head"]/a/text()').extract()
        item['description'] = response.xpath('//div[@class="event_body"]/table/tr[3]/td[@class="right"]text()').extract()
        return item