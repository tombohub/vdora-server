"""Script for importing inventory transactions into Transaction inventory model
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


with open('transac.csv') as csvfile:
    from inventory.models import Transaction, Product, Location, TransactionType

    reader = csv.DictReader(csvfile)
    for row in reader:
        date = row['Date']
        product = Product.objects.get(sku=row['SKU'])
        type = TransactionType.objects.get(type=row['Transaction Type'])
        quantity = row['Quantity']
        location = Location.objects.get(location=row['Location'])
        note = row['Note']

        transaction = Transaction(
            date=date, product=product, type=type, quantity=quantity, location=location, note=note)
        transaction.save()
