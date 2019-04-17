# -*- coding: utf-8 -*-
import scrapy

class DreamlandSpider(scrapy.Spider):
    name = 'dreamland'
    start_urls = (
        'http://www.dreamlandbbs.com/filegate/gamesnet/pda/index.html',
        'http://www.dreamlandbbs.com/filegate/gamesnet/pda/pilot/index.html',
        'http://www.dreamlandbbs.com/filegate/utilnet/utilpt/index.html'
    )

    def parse(self, response):
        for row in response.css('tr'):
            yield {
                'url': row.css('a::attr(href)').get(),
                'description': row.css('pre::text').get(),
            }

        next_page = response.xpath("//a[contains(., 'Next')]/@href").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
