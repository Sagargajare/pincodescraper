import scrapy

from pincodescraper.items import PincodescraperItem
from .run import getAlllinks
class PincodeSpider(scrapy.Spider):
    name = 'pincode'
    allowed_domains = ['https://www.indiatvnews.com/']
    # start_urls = ['https://www.indiatvnews.com/pincode/maharashtra/beed/ambewadgaon/']
    start_urls =getAlllinks()

    def parse(self, response):
        item = PincodescraperItem()
        response = response.css(".pin-details  tr")
        lst = []
        for i in range(1,len(response)):
            lst.append(response[i].css('td::text').extract())
            # yield {'text':response[i].css('td::text').extract()}

        item["Pincode"] 	= lst[0][1]
        item["Taluk"] = lst[1][1]
        item["Division"] = lst[2][1]
        item["District"] 	= lst[3][1]
        item["Region"] = lst[4][1]
        item["Circle"] 	= lst[5][1]
        item["State"] 	= lst[6][1]
        item["Country"] 	= lst[7][1]
        item["TelephoneNo"]  = lst[8][1]
        item["OfficeType"] 	= lst[9][1]
        item["DeliveryStatus"] 	= lst[10][1]
        item["RelatedSubOffice"]  = lst[11][1]
        item["RelatedHeadOffice"] = lst[12][1]

        yield item
