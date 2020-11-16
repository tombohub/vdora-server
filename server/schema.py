import graphene
from graphene_django import DjangoObjectType
from sales.models import Sale, NooksPayoutSchedule


class SaleType(DjangoObjectType):
    class Meta:
        model = Sale


class NooksPayoutType(DjangoObjectType):
    class Meta:
        model = NooksPayoutSchedule


class Query(graphene.ObjectType):
    sales = graphene.List(SaleType)
    payouts = graphene.List(NooksPayoutType)

    def resolve_sales(root, info):
        return Sale.objects.select_related('nooks_payout_schedule').all()

    def resolve_payouts(root, info):
        return NooksPayoutSchedule.objects.all()


schema = graphene.Schema(query=Query)
