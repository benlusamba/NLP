import scrapy


class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    allowed_domains = ['https://www.nytimes.com/section/business?action=click&pgtype=Homepage&region=TopBar&module=HPMiniNav&contentCollection=Business&WT.nav=page']
    start_urls = ['https://www.nytimes.com/section/business?action=click&pgtype=Homepage&region=TopBar&module=HPMiniNav&contentCollection=Business&WT.nav=page']

    def parse(self, response):
        pass
        Headlines = response.css(".headline::text").extract()
        Summary = response.css(".summary::text").extract()
        Byline = response.css(".byline::text").extract()

        for item in zip(Headlines,Summary,Byline):
            #create a dictionary for scraped info
            scraped_info = {
                'Headlines' : item[0],
                'Summary' : item[1],
                'Byline' : item[2]
            }

            yield scraped_info
