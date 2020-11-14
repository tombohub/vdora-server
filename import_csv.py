"""Script for importing sales into Sale model from csv
    """


import csv
import os
import sys
import django

# Django configuration
sys.path.append(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'
django.setup()


with open('sales.csv') as csvfile:
    from sales.models import Sale
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = row['Sale Date']
        sale_id = row['Sale ID']
        sku = row['SKU']
        product = row['Product Name']
        quantity = row['Quantity']
        price = row['Price']
        channel = row['Channel']

        sale = Sale(date=date, sale_id=sale_id, sku=sku, product=product,
                    quantity=quantity, price=price, channel=channel)
        sale.save()
