import scrapy
import jsonlines
import json
import uuid
import io

class LiveCongressSpider(scrapy.Spider):

    name = "livecongress"
    start_urls = ["https://www.livecongress.it/aol/index.php?id=B6348358"]

    def parse(self, response):
        date_event = response.xpath("//div[@class='sinDayHeader']/text()").getall()
        # print("======>{0}".format(data_event))
        fp = io.BytesIO()
        with jsonlines.open("D:/airfinity_demo/output.jsonl", mode='w') as wr:
            for item_date in date_event:
                entity = {"id": str(uuid.uuid4()), "date_content": item_date}
                wr.write(entity)
        wr.close()
        fp.close()
        pass
