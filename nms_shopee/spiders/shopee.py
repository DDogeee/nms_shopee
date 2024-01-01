import scrapy
import logging
from scrapy.utils.log import configure_logging 

class ShopeeSpider(scrapy.Spider):
    # configure_logging(install_root_handler=False)
    # logging.basicConfig(
    #     filename='log.txt',
    #     format='%(levelname)s: %(message)s',
    #     level=logging.INFO
    # )
    name = "shopee"
    allowed_domains = ["shopee.vn"]
    start_urls = ["https://shopee.vn/api/v4/pages/get_category_tree"]
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    def parse_cate(self, response):
        parent_name = response.meta.get('parent_name')
        r = response.json()
        items = r['data']['sections'][0]['data']['item']
        if items is not None:
            for item in items:
                try:
                    yield {
                        "category" : parent_name,
                        "product_name": item['name'],
                        "product_url" : f"https://shopee.vn/a-i.{item['shopid']}.{item['itemid']}",
                        "product_rating": item['item_rating']['rating_star'],
                        "product_price": item['price'],
                        "product_revenue" : item['price']*item['historical_sold']
                    }
                except:
                    pass

    def parse(self, response):
        r = response.json()
        # self.log(response)
       
        for parent in r['data']['category_list']:
            for child in parent['children']:
                yield scrapy.Request(url = f"https://shopee.vn/api/v4/recommend/recommend?bundle=category_landing_page&catid={child['catid']}&limit=500", callback=self.parse_cate, meta = {"parent_name" : parent['display_name']})
              
