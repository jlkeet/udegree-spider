from ntpath import join
import scrapy
import re
import datetime
from dateutil.parser import parse
from datetime import timedelta


class QuotesSpider(scrapy.Spider):
    name = "Melbourne"
    course_data = {}

    def start_requests(self):    

        urls = [
              "https://handbook.unimelb.edu.au/search?types%5B%5D=subject",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
          for href in response.xpath('//a[@class="search-result-item__anchor"]/@href'):
             yield response.follow(href, self.parse_dir_contents)

    def parse_dir_contents(self, response):
            self.log("Starting Scraper")
            newUrl = str(response)[5:-1] + '/eligibility-and-requirements'
            item =  {
                    'name': response.xpath('//meta[@name="short_title"]/@content').get(), 
                    'title': response.xpath('//meta[@name="code"]/@content').get(),
                    'desc': response.xpath('//div[@class="course__overview-wrapper clearfix"]//p/text()').get(),
                    # 'faculties': response.xpath('//h2[@class="b8"]/text()').get().strip(' ')[-1],
                    # 'department': response.xpath('//h1/text()').get().strip(),
                    'points': response.xpath('//meta[@name="points"]/@content').get(),
                    'stage': response.xpath('//meta[@name="level"]/@content').get()[-1],
                     }
            yield scrapy.Request(url=newUrl, callback=self.parse_requirements, meta={'item': item})

    def parse_requirements(self, response):
        self.log("Parsing Requirements")
        item = response.meta['item']
        item['requirements'] = response.xpath("//td[1]//text()").getall()
        yield item