# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscrapperScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    job_link = scrapy.Field()
    company_name = scrapy.Field()
    job_location = scrapy.Field()
    job_salary = scrapy.Field()
    job_posted = scrapy.Field()
    job_description = scrapy.Field()
    posted_website = scrapy.Field()
