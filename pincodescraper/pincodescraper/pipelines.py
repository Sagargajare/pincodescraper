# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging
username = 'pincode'
pawd = 'pincode123'
uri =f'mongodb+srv://{username}:{pawd}@cluster0.zrczi.mongodb.net'
dbname = 'pincode'
# myclient = pymongo.MongoClient(f"")
class PincodescraperPipeline:
    collection_name = 'pincode'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=uri,
            mongo_db=dbname
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        self.db[self.collection_name].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item
    # def __init__(self):
    #     self.create_connection()
    #     self.createTable()
    # def process_item(self, item, spider):
    #     self.store_db(item)
    #     return item
    # def create_connection(self):
    #     self.conn = sqlite3.connect('databse.db')
    #     self.curr = self.conn.cursor()
    # def createTable(self):
    #     self.curr.execute('''DROP TABLE IF EXISTS PINCODE''')
    #     self.curr.execute("""CREATE TABLE PINCODE(
    #         Pincode  TEXT    NOT NULL,
    #         Taluk  TEXT     NOT NULL,

    #         Division  TEXT    NOT NULL,
    #         Region   TEXT     NOT NULL,
    #         Circle  TEXT    NOT NULL,
    #         State  TEXT     NOT NULL,
    #         Country   TEXT    NOT NULL,
    #         TelephoneNo    TEXT     NOT NULL,
    #         OfficeType     TEXT    NOT NULL,
    #         DeliveryStatus   TEXT     NOT NULL,
    #         RelatedSubOffice TEXT    NOT NULL,
    #         RelatedHeadOffice TEXT     NOT NULL,
    #         )""")
    # def store_db(self,item):
    #     self.conn.execute("""insert into PINCODE values (? ,?, ?)""")(
    #         item["Pincode"],
    #         item["Taluk"],
    #         item["Division"],
    #         item["District"] ,
    #         item["Region"],
    #         item["Circle"],
    #         item["State"],
    #         item["Country"] ,
    #         item["TelephoneNo"],
    #         item["OfficeType"],
    #         item["DeliveryStatus"] ,
    #         item["RelatedSubOffice"],
    #         item["RelatedHeadOffice"],
    #     )
    #     self.conn.commit()