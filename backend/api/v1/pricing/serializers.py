from pricing.models import Pricing,UserCart,PaidPackageInfo
from rest_framework import serializers


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pricing
        exclude = ('active','created_at')

class PostPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pricing
        fields='__all__'

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


class ShortPaidPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pricing
        fields=['name']

class PaidPackageSerializer(serializers.ModelSerializer):
    # package=ShortPaidPackageSerializer(read_only=True)
    class Meta:
        model= PaidPackageInfo
        fields = ['id','remaining_items','created_at','expired_at']


class UsePackageSerializer(serializers.Serializer):
    package_id=serializers.IntegerField()
    draft_id=serializers.UUIDField()

    class Meta:
        fields=['package_id','draft_id']
