import scrapy
from ..items import JobscrapperScrapyItem

class SimplyHired(scrapy.Spider):
    name = "simplyhired"
    # Allowed_domains will allow only given domains in the list while scraping the website and
    # ignore all other domains present in the site
    allowed_domains = [
        'www.simplyhired.ca'
    ]

    # Initialising the filter(job_title, job_location using __init__ method
    def __init__(self, job_title='machine learning'):
        job_title = job_title.replace(' ', '+')
        self.start_urls = [f'https://www.simplyhired.ca/search?q={job_title}&l=']
        super().__init__()

    # Main script that parse the scrapy with all the items given
    def parse(self, response, **kwargs):
        item = JobscrapperScrapyItem()
        # From website getting to know about the template that holds all the details and making them to a list
        job_list = response.xpath('//article/div[@class="SerpJob-jobCard card"]')
        for job in job_list:

            # From the list obtained above, extracting job title using Xpath
            job_title = job.xpath('.//div[@class="jobposting-title"]/a/text()').extract()
            job_title = "".join(job_title)  # Using join to extract the strings from list or can use extract()[0]

            # From the list obtained above, extracting job_link using Xpath
            job_link = job.xpath('.//div[@class="jobposting-title"]/a/@href').extract()
            job_link = "".join(job_link)
            job_link = "https://www.workopolis.com" + job_link

            # From the list obtained above, extracting company_name using Xpath
            company_name = job.xpath('.//div/span[@class="JobPosting-labelWithIcon jobposting-company"]/text()').extract()
            company_name = "".join(company_name)

            # From the list obtained above, extracting job_description using Xpath
            job_description = job.xpath('.//div/p[@class="jobposting-snippet"]/text()').extract()
            job_description = "".join(job_description)

            # From the list obtained above, extracting job_location using Xpath
            job_location = job.xpath('.//div//span[@class="jobposting-location"]/text()').extract()
            job_location = "".join(job_location)

            # From the list obtained above, extracting job_salary using Xpath
            job_salary = job.xpath('.//div[@class="SerpJob-metaInfoLeft"]/span//text()').extract()
            job_salary = "".join(job_salary)

            # From the list obtained above, extracting job_posted using Xpath
            job_posted = job.xpath('.//div[@class="SerpJob-metaInfoRight"]/span//text()').extract()
            job_posted = "".join(job_posted)

            # From all variables above, appending the data to items
            item["job_title"] = job_title
            item["job_link"] = job_link
            item["company_name"] = company_name
            item["job_location"] = job_location
            item["job_salary"] = job_salary
            item["job_posted"] = job_posted
            item["job_description"] = job_description
            item["posted_website"] = "SimplyHired"

            yield item

        # Finding link of next page until it goes to last page
        pages = response.xpath('//li[@class="next-pagination"]')
        next_page = pages.xpath('./a//@href').get()

        # if next is present then, call the parse method again to scrape next page
        if next_page is not None:
            next_page = "https://www.simplyhired.ca" + next_page
            yield response.follow(next_page, callback=self.parse)
