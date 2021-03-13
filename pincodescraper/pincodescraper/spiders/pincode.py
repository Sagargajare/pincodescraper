import scrapy

from pincodescraper.items import PincodescraperItem
from .run import getAlllinks
def unique(list1):
     
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    unique_list = (list(list_set))
    return unique_list
class PincodeSpider(scrapy.Spider):
    name = 'pincode'
    allowed_domains = ['https://www.indiatvnews.com/']
    # start_urls = ['https://www.indiatvnews.com/pincode/maharashtra/beed/ambewadgaon/']
    start_urls =unique(getAlllinks())

    def parse(self, response):
        item = PincodescraperItem()
        response1 = response.css(".pin-details  tr")
        lst = []
        for i in range(1,len(response1)):
            lst.append(response1[i].css('td::text').extract())
            # yield {'text':response[i].css('td::text').extract()}
        item["Office"] 	= response.css(".pin-details  tr th::text")[1].get()
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
