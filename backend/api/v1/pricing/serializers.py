from pricing.models import Pricing,UserCart
from rest_framework import serializers


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pricing
        exclude = ('active','created_at')

class CartPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pricing
        fields=['id','price','items','name','duration_month']


class UserCartSerializer(serializers.ModelSerializer):
    package = CartPricingSerializer(read_only=True)
    class Meta:
        model= UserCart
        fields = ['id','created_at','package','quantity']

class PostCartSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserCart
        fields = ['package']

