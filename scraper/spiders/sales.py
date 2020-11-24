import scrapy
from decouple import config
from scrapy.http import headers
from scraper.items import SaleItem
from sales.models import Sale
from django.db.models import Max


def authentication_failed(response):
    pass


class SalesSpider(scrapy.Spider):
    """Login to nooks, get the order list JSON, based on order.id go to details page
    and parse the further details from there now called sale details

    Yields:
        dict: Sale Item with details
    """
    name = 'sales'
    start_urls = ['http://sell.thenooks.ca/index.php?p=login']
    handle_httpstatus_list = [403]

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
                                                callback=self.after_login,
                                                )

    def after_login(self, response):
        """After login we will grab the issue request for order data
        """
        if authentication_failed(response):
            self.logger.error("Login failed")
            return
        url = config('ORDERS_API_URL')
        yield scrapy.Request(url=url, callback=self.parse_orders)

    def parse_orders(self, response):
        '''getting orders data available from orders listing page'''

        orders = response.json().get('data')

        # we are gonna scrape sale details only if it is later than
        # nooks last sale_id in database
        last_sale_id = Sale.objects.filter(channel='Nooks').aggregate(
            Max('sale_id'))['sale_id__max']

        for order in orders:
            if int(order['id']) > last_sale_id:
                sale = SaleItem()
                sale['sale_id'] = order['id']

                # slice because order['date_add'] is yyyy-mm-dd hh-mm-ss format
                sale['date'] = order['date_add'][:10]

                order_url = f'http://sell.thenooks.ca/index.php?p=order_desc&oid={order["id"]}&status=fulfilled'
                yield scrapy.Request(url=order_url, callback=self.parse_order_details, meta={'item': sale})

    def parse_order_details(self, response):
        """ Parsing sale details after getting order id"""

        sale = response.meta['item']
        rows = response.css('div.mp-table table tbody tr')
        for row in rows:
            sale['product'] = row.css('td:nth-child(2) a::text').get()
            sale['sku'] = row.css('td:nth-child(3)::text').get()
            sale['quantity'] = row.css('td:nth-child(4)::text').get()
            sale['price'] = row.css(
                'td:nth-child(5) span.price::text').get()
            yield sale
