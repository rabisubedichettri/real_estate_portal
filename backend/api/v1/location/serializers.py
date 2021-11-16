from location.models import (Provience,District,SubDistrict,Ward)
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class ProvienceReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provience
        fields=['id',"name"]

class DistrictReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields=['id',"name"]

class SubDistrictReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubDistrict
        fields=['id',"name"]

class WardReadSeraializer(serializers.ModelSerializer):
    class Meta:
        model=Ward
        fields=["id","name"]