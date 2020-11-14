"""Script to update Sale model with payout schedule reference
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
    from sales.models import Sale, NooksPayoutSchedule
