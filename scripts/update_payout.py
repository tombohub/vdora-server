"""Script to update Sale model with payout schedule reference foreign key
    """

import os
import sys
import django

# Django configuration
sys.path.append(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'
django.setup()


def update_payouts():
    """update Sale.nook_payout_schedule with refeence to nook payout schedule table 
    if sale date is in between schedule and sale channel is nooks
    """
    from sales.models import Sale, NooksPayoutSchedule
    schedules = NooksPayoutSchedule.objects.all()
    sales = Sale.objects.all()

    for schedule in schedules:
        for sale in sales:
            if sale.date >= schedule.start_date and sale.date <= schedule.end_date:
                if sale.channel == 'Nooks':
                    sale.nooks_payout_schedule = schedule
                else:
                    sale.nook_payout_schedule = None
                sale.save()


update_payouts()
