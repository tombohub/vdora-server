import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from sales.models import Sale, NooksPayoutSchedule
from inventory.models import Transaction, Location, TransactionType, Product, Test, Kaka
from inventory.serializers import TransactionSerializer


class SaleType(DjangoObjectType):
    class Meta:
        model = Sale


class NooksPayoutType(DjangoObjectType):
    class Meta:
        model = NooksPayoutSchedule


class TransactionGraphqlType(DjangoObjectType):
    class Meta:
        model = Transaction


class TransactionTypeType(DjangoObjectType):
    class Meta:
        model = TransactionType


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(graphene.ObjectType):
    sales = graphene.List(SaleType)
    payouts = graphene.List(NooksPayoutType)
    transactions = graphene.List(TransactionGraphqlType)
    transaction_types = graphene.List(TransactionTypeType)
    locations = graphene.List(LocationType)
    products = graphene.List(ProductType)

    def resolve_sales(root, info):
        return Sale.objects.select_related('nooks_payout_schedule').all()

    def resolve_payouts(root, info):
        return NooksPayoutSchedule.objects.all()

    def resolve_transactions(root, info):
        return Transaction.objects.all()

    def resolve_transaction_types(root, info):
        return TransactionType.objects.all()

    def resolve_locations(root, info):
        return Location.objects.all()

    def resolve_products(root, info):
        return Product.objects.all()


class TestType(DjangoObjectType):
    class Meta:
        model = Test


class KakaType(DjangoObjectType):
    class Meta:
        model = Kaka


class TestMutation(graphene.Mutation):
    # koko = graphene.String()
    # momo = graphene.Int()

    test = graphene.Field(TestType)
    kaka = graphene.Field(KakaType)

    class Arguments:
        koko = graphene.Int()
        momo = graphene.Int()

    def mutate(self, info, momo, koko):
        test = Test(momo=momo)
        kaka = Kaka(kaka=koko)
        test.save()
        kaka.save()

        return TestMutation(test=test, kaka=kaka)


class TransactionMutation(SerializerMutation):
    class Meta:
        serializer_class = TransactionSerializer


class Mutation(graphene.ObjectType):
    test_mutation = TestMutation.Field()
    transaction_mutation = TransactionMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
