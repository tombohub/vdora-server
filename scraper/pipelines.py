# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sales.models import Sale, NooksPayoutSchedule
from inventory.models import Transaction, Product, TransactionType, Location


class SaleDatabasePipeline:
    def process_item(self, item, spider):
        if Sale.objects.filter(sale_id=item['sale_id']).exists():
            print('Sale already exists in database')
            return item
        else:
            sale = Sale()
            sale.sale_id = item['sale_id']
            sale.date = item['date']
            sale.sku = item['sku']
            sale.product = item['product']
            sale.quantity = item['quantity']
            sale.price = item['price']
            sale.channel = 'Nooks'

            # attribute nooks payout period to the sale
            nooks_payout_schedule = NooksPayoutSchedule.objects.get(
                start_date__lte=sale.date, end_date__gte=sale.date)
            sale.nooks_payout_schedule = nooks_payout_schedule

            # record change in inventory because of sale
            transaction = Transaction()
            transaction.date = item['date']
            transaction.product = Product.objects.get(sku=item['sku'])
            transaction.type = TransactionType.objects.get(
                id=1)  # id 1 is Sale
            transaction.quantity = -item['quantity'] # minus because it's sale
            transaction.location = Location.objects.get(id=1)  # id 1 is Nooks

            sale.save()
            transaction.save()
            return item
