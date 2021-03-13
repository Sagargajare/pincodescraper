# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PincodescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Pincode	= scrapy.Field()
    Taluk	= scrapy.Field()
    Division= scrapy.Field()
    District	= scrapy.Field()
    Region= scrapy.Field()
    Circle	= scrapy.Field()
    State	= scrapy.Field()
    Country	= scrapy.Field()
    TelephoneNo = scrapy.Field()
    OfficeType	= scrapy.Field()
    DeliveryStatus	= scrapy.Field()
    RelatedSubOffice = scrapy.Field()
    RelatedHeadOffice = scrapy.Field()
