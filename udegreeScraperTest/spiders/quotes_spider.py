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
            self.log("starting scrape 23")
            newUrl = str(response)[5:-1] + '/eligibility-and-requirements'
            #self.log(newUrl)
            item =  {
                    'name': response.xpath('//meta[@name="short_title"]/@content').get(), 
                    'title': response.xpath('//meta[@name="code"]/@content').get(),
                    'desc': response.xpath('//div[@class="course__overview-wrapper clearfix"]//p/text()').get(),
                    # 'faculties': response.xpath('//h2[@class="b8"]/text()').get().strip(' ')[-1],
                    # 'department': response.xpath('//h1/text()').get().strip(),
                    'points': response.xpath('//meta[@name="points"]/@content').get(),
                    'stage': response.xpath('//meta[@name="level"]/@content').get()[-1],
                    # 'restrictions': response.xpath('//p[@class="prerequisite"]//i/text()').getall()[0].strip()
                     }
            yield scrapy.Request(url=newUrl, callback=self.parse_requirements, meta={'item': item})

    def parse_requirements(self, response):
        item = response.meta['item']
        item['requirements'] = response.xpath("//td[1]//text()").getall()
        yield item


    # def start_requests(self):
    #     urls = [
    #         'https://handbook.unimelb.edu.au/search?study_periods%5B%5D=all&area_of_study%5B%5D=all&types%5B%5D=subject&year=2022&level_type%5B%5D=all&campus_and_attendance_mode%5B%5D=all&org_unit%5B%5D=all&page=1&sort=external_code%7Casc',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #         self.log("starting scrape")

    #         yield { # possibly best to loop through for each of these.
    #             'name': response.xpath('//span[@class="search-result-item__code"]/text()').getall(), # can strip later
    #             'title': response.xpath('//div[@class="search-result-item__name"]/h3/text()').getall(), # can strip later
    #             'desc': response.xpath('//p[@class="description"]/text()').getall()[0].strip(), # can strip later
    #             'faculties': response.xpath('//h2[@class="b8"]/text()').get().strip(' ')[-1],
    #             'department': response.xpath('//h1/text()').get().strip(),
    #             'points': response.xpath('//div[@class="search-result-item__meta-secondary"]/text()').getall()[0].strip(), # can strip later
    #             'stage': response.xpath('//div[@class="search-result-item__meta-secondary"]/text()').getall()[1].strip()[-3],
    #             'restrictions': response.xpath('//p[@class="prerequisite"]//i/text()').getall()[0].strip() # this is the hard part, this will give us the restrictions but we must create logic to parse them with normal language. eeeek.
    #         }