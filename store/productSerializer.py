from decimal import Decimal
from rest_framework import serializers
from  .models import Product, Collection


class CollectionSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class productSerializerFunction(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    outprice = serializers.DecimalField(max_digits=6, decimal_places=2, source='price')
    id = serializers.IntegerField()
    price_increase = serializers.SerializerMethodField(method_name='priceadd')
    collection = CollectionSerializers()

    def priceadd(self, product: Product):
        return product.price * Decimal(3.1)