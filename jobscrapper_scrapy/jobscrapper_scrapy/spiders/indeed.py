import scrapy
from ..items import JobscrapperScrapyItem


class IndeedSpider(scrapy.Spider):
    name = 'indeed'

    def __init__(self, job_title='Data Science'):
        job_title = job_title.replace(' ', '+')
        self.start_urls = [f'https://ca.indeed.com/jobs?q={job_title}'+'&l=']
        super().__init__()

    def parse(self, response):

        # Creating an object of items
        item = JobscrapperScrapyItem()
        job_postings = response.xpath('//div[@data-tn-component="organicJob"]')

        # Looping through all job postings in the page
        for job in job_postings:
            # Job title
            job_title = job.xpath('.//h2/a/@title').extract()
            job_title = "".join(job_title)

            # Job Link
            job_link = job.xpath('.//h2/a/@href').extract()
            job_link = "".join(job_link)
            job_link = "https://ca.indeed.com" + job_link

            # Company
            company_name = job.xpath('.//span[@class="company"]/text()').extract()
            company_name = "".join(company_name)
            if company_name == '\n':
                company_name = job.xpath('.//span[@class="company"]/a/text()').extract()
                company_name = "".join(company_name)
            company_name = company_name.strip('\n')

            # Location
            job_location = job.xpath('.//span[@class="location accessible-contrast-color-location"]/text()').extract()
            job_location = "".join(job_location)

            # Salary
            job_salary = job.xpath('.//span[@class="salaryText"]/text()').extract()
            job_salary = "".join(job_salary)
            job_salary = job_salary.strip('\n')

            # Posted on
            job_posted = job.xpath('.//span[@class="date "]/text()').extract()
            job_posted = "".join(job_posted)

            # Short description
            summary = job.xpath('.//div[@class="summary"]//li')
            job_description = []
            for line in summary:
                job_description.append("".join(line.xpath('./text()').extract()))

            # Creating an item with data
            item['job_title'] = job_title
            item['job_link'] = job_link
            item['company_name'] = company_name
            item['job_location'] = job_location
            item['job_salary'] = job_salary
            item['job_posted'] = job_posted
            item['job_description'] = job_description
            item['posted_website'] = "Indeed.ca"

            # return the scrapped data using yield
            yield item

        # Finding link of next page
        pages = response.xpath('//ul[@class="pagination-list"]//li')
        next_page = pages[-1].xpath('.//a/@href').get()

        if next_page is not None:
            next_page = "https://ca.indeed.com" + next_page
            yield response.follow(next_page, callback=self.parse)
