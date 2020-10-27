# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sales.models import Sale


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

            sale.save()

            return item
