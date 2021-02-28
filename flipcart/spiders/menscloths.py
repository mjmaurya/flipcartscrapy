import scrapy
from ..items import FlipcartItem

class MensclothsSpider(scrapy.Spider):
    name = 'menscloths'
    next_page=2
    start_urls = ['https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo%2Cash&otracker=categorytree&p%5B%5D=facets.ideal_for%255B%255D%3DMen&page=1']

    def parse(self, response):
        items=FlipcartItem()
        products=response.css("div._1xHGtK")
        for product in products:
            name = product.css(".IRpwTa::text").extract()
            brand = product.css("._2WkVRV::text").extract()
            original_price = product.css("._3I9_wc::text").extract()[1]
            sale_price = product.css("._30jeq3::text").extract()[0][1:]
            image_url = product.css("._2r_T1I::attr('src')").extract()
            product_page_url = "https://www.flipkart.com"+product.css("._2UzuFa::attr('href')").extract()[0]
            product_category = "men topwear"

            items["name"]=name
            items["brand"]=brand
            items["original_price"]=original_price
            items["sale_price"]=sale_price
            items["image_url"]=image_url
            items["product_page_url"]=product_page_url
            items["product_category"]=product_category
            yield items

            
