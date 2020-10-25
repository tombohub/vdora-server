import scrapy
from decouple import config
from scraper.items import Sale


def authentication_failed(response):
    pass


class SalesSpider(scrapy.Spider):
    name = 'sales'
    start_urls = ['http://sell.thenooks.ca/index.php?p=login']
    sale = Sale()

    def parse(self, response):
        """Logins and grabs the session to get the orders data
        """
        formdata = {
            'wk_email': config('WK_EMAIL'),
            'wk_password': config('WK_PASSWORD')
        }
        return scrapy.FormRequest.from_response(response,
                                                formdata=formdata,
                                                formid='login_form',
                                                callback=self.after_login
                                                )

    def after_login(self, response):
        """After login we will grab the issue request for order data
        """
        if authentication_failed(response):
            self.logger.error("Login failed")
            return
        url = 'http://sell.thenooks.ca/index.php?p=order'
        yield scrapy.Request(url=url, callback=self.parse_orders)

    def parse_orders(self, response):
        '''getting orders data available from orders listing page'''
        orders = response.css('div.mp-table tbody tr')
        print(response.text)
        for order in orders:
            print(order)
            self.sale['id'] = order.css('td.sorting_1::text').get()
            self.sale['date'] = order.css('td:nth-child(3)::text').get()

            #     order_url = f'http://sell.thenooks.ca/index.php?p=order_desc&oid={order["id"]}&status=fulfilled'
            #     yield scrapy.Request(url=order_url, callback=self.parse_order_details)

        order_url = f'http://sell.thenooks.ca/index.php?p=order_desc&oid=2182212&status=fulfilled'
        yield scrapy.Request(url=order_url, callback=self.parse_order_details)

    def parse_order_details(self, response):
        rows = response.css('div.mp-table table tbody tr')
        for row in rows:
            self.sale['product'] = row.css('td:nth-child(2) a::text').get()
            self.sale['sku'] = row.css('td:nth-child(3)::text').get()
            self.sale['quantity'] = row.css('td:nth-child(4)::text').get()
            self.sale['price'] = row.css(
                'td:nth-child(5) span.price::text').get()
            yield self.sale
