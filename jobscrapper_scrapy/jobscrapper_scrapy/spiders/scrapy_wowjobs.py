import scrapy
from ..items import JobscrapperScrapyItem
from scrapy.spiders import Spider


class wowjobs(scrapy.Spider):
    name = "wowjobs"
    # allowed_domains allows only given domains in the list while scraping the website and ignore all other domains present in the site
    allowed_domains = [
        'www.wowjobs.ca'
    ]

    # Initialising the filter(job_title, job_location using __init__ method
    def __init__(self, job_title='machine learning', job_location='Toronto'):
        job_title = job_title.replace(' ', '+')
        job_location = job_location.replace(' ', '+')
        self.start_urls = [f'https://www.wowjobs.ca/BrowseResults.aspx?q={job_title}&l={job_location}']
        super().__init__()
                #https://www.wowjobs.ca/BrowseResults.aspx?q=machine+learning&l=Toronto

    # Main script that parse the scrapy with all the items given
    def parse(self, response, **kwargs):
        item = JobscrapperScrapyItem()
        #from website getting to know about the template that holds all the details and making them to a list
        job_list = response.xpath('//div[@class="result js-job"]')
        for job in job_list:

            # From the list obtained above, extracting job title using Xpath
            job_title = job.xpath('.//div/a/text()').extract()
            job_title = "".join(job_title)  # Using join to extract the strings from list or can use extract()[0]
            # From the list obtained above, extracting job_link using Xpath

            job_link = job.xpath('.//div/a/@href').extract()
            job_link = "".join(job_link)
            job_link = "https://www.wowjobs.ca" + job_link

            # From the list obtained above, extracting company_name using Xpath
            company_name = job.xpath('.//div[@class="employer"]/text()').extract()
            company_name = "".join(company_name)

            # From the list obtained above, extracting job_description using Xpath
            job_description = job.xpath('.//div[@class="snippet"]/text()').extract()
            job_description = "".join(job_description)

            # From the list obtained above, extracting job_location using Xpath
            job_location = job.xpath('.//div[@class="employer"]/span/text()').extract()
            job_location = "".join(job_location)

            # From the list obtained above, there no data available for job_salary
            job_salary = 'N/A'

            # From the list obtained above, extracting job_posted using Xpath
            job_posted = job.xpath('.//div[@class="tags"]/text()').extract()
            job_posted = "".join(job_posted)
            if job_posted is '':
                job_posted = 'N/A'

            # From all variables above, appending the data to items
            item["job_title"] = job_title
            item["job_link"] = job_link
            item["company_name"] = company_name
            item["job_location"] = job_location
            item["job_salary"] = job_salary
            item["job_posted"] = job_posted
            item["job_description"] = job_description
            item["posted_website"] = "www.wowjobs.ca"

            yield item

        # Finding link of next page until it goes to last page
        #pages = response.xpath('//div[@class="paging"]')
        #next_page = pages.xpath('./a//@href').get()
        #next_ = response.xpath('//div/a[@class="btn btn-primary PageText"]/text()').get()
        next_page = response.css(".paging").xpath('./a//@href').get()

        #if next is present then, call the parse method again to scrape next page
        if next_page is not None:
            next_page = "https://www.wowjobs.ca" + next_page
            yield response.follow(next_page, callback=self.parse, dont_filter=False)
