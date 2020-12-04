import scrapy
from ..items import JobscrapperScrapyItem

class Workopolis(scrapy.Spider):
    name = "workopolis"
    # allowed_domains will allow only given domains in the list while scraping the website and
    # ignore all other domains present in the site
    allowed_domains = [
        'www.workopolis.com'
    ]

    # Initialising the filter(job_title, job_location using __init__ method
    def __init__(self, job_title='machine-learning'):
        job_title = job_title.replace('-', '+')
        self.start_urls = [f'https://www.workopolis.com/jobsearch/find-jobs?ak={job_title}' + '&l=']
        super().__init__()

    # Main script that parse the scrapy with all the items given
    def parse(self, response, **kwargs):
        item = JobscrapperScrapyItem()
        # from website getting to know about the template that holds all the details and making them to a list
        job_list = response.xpath('//article[@class="JobCard"]')

        for job in job_list:

            # From the list obtained above, extracting job title using Xpath
            job_title = job.xpath('.//h2[@class="JobCard-title"]/a/text()').extract()
            job_title = "".join(job_title)  # Using join to extract the strings from list or can use extract()[0]

            # From the list obtained above, extracting job_link using Xpath
            job_link = job.xpath('.//h2[@class="JobCard-title"]/a/@href').extract()
            job_link = "".join(job_link)
            job_link = "https://www.workopolis.com" + job_link

            # From the list obtained above, extracting company_name using Xpath
            company_name = job.xpath('.//div[@class="JobCard-property JobCard-company"]/span/text()').extract()
            company_name = "".join(company_name)

            # From the list obtained above, extracting job_description using Xpath
            job_description = job.xpath('.//div[@class="JobCard-snippet"]/text()').extract()
            job_description = "".join(job_description)

            # From the list obtained above, extracting job_location using Xpath
            job_location = job.xpath('.//span[@class="JobCard-property JobCard-location"]/span/text()[2]').extract()
            job_location = "".join(job_location)

            # From the list obtained above, extracting job_salary using Xpath
            job_salary = job.xpath('.//span[@class="Salary"]/text()').extract()
            job_salary = "".join(job_salary)

            # From the list obtained above, extracting job_posted using Xpath
            job_posted = job.xpath('.//time[@class="JobCard-property JobCard-age"]/text()').extract()
            job_posted = "".join(job_posted)

            # From all variables above, appending the data to items
            item["job_title"] = job_title
            item["job_link"] = job_link
            item["company_name"] = company_name
            item["job_location"] = job_location
            item["job_salary"] = job_salary
            item["job_posted"] = job_posted
            item["job_description"] = job_description
            item["posted_website"] = "Workopolis"

            yield item

        # Finding link of next page until it goes to last page
        pages = response.xpath('//div/span/a[@class="Pagination-link Pagination-link--next"]')
        next_page = pages.xpath('.//@href').get()

        # if next is present then, call the parse method again to scrape next page
        if next_page is not None:
            next_page = "https://www.workopolis.com" + next_page
            yield response.follow(next_page, callback=self.parse)
