# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sales.models import Sale, NooksPayoutSchedule
from inventory.models import Transaction, Product, TransactionType, Location
from django.db.models import Q


class SaleDatabasePipeline:
    def process_item(self, item, spider):

        # / SALE >>>>

        # extra if check up. shouldn't trigger because we already only scraping since th last sale.
        if Sale.objects.filter(sale_id=item['sale_id'], product__sku=item['sku']).exists():
            print('Sale already exists in database')
            return item
        else:
            sale = Sale()
            sale.sale_id = item['sale_id']  # nooks sale id
            sale.date = item['date']
            sale.product = Product.objects.get(
                Q(sku=item['sku']) | Q(sku_oshawa=item['sku']))
            sale.quantity = item['quantity']
            sale.price = item['price'][1:]  # slice bcause first char is $

            sale.channel = 'Nooks'

            # attribute nooks payout period to the sale
            nooks_payout_schedule = NooksPayoutSchedule.objects.get(
                start_date__lte=sale.date, end_date__gte=sale.date)
            sale.nooks_payout_schedule = nooks_payout_schedule

            sale.save()

            # / TRANSACTION >>>>

            # record change in inventory because of sale
            transaction = Transaction()
            transaction.date = item['date']
            transaction.product = sale.product
            transaction.type = TransactionType.objects.get(
                id=1)  # id 1 is Sale

            # minus because it's sale
            transaction.quantity = -int(item['quantity'])
            transaction.location = Location.objects.get(
                name=item['location'])

            # because each location has different sku need to check which sku to query
            # all because one sale id can be multiple items.
            # TODO: redesign

            if item['location'] == "Oshawa Centre":  # for now only check oshawa
                transaction.sale = Sale.objects.get(
                    sale_id=item['sale_id'], product__sku_oshawa=item['sku'])
            else:
                transaction.sale = Sale.objects.get(
                    sale_id=item['sale_id'], product__sku=item['sku'])

            transaction.save()
            return item
