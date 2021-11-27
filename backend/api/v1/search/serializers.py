from rest_framework import serializers
from listing.models import Listing
from location.models import Ward,District,SubDistrict,Provience


class ProvienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provience
        fields='__all__'


class DistrictSerializer(serializers.ModelSerializer):
    provience=ProvienceSerializer(read_only=False)
    class Meta:
        model=District
        fields="__all__"

# class SubDistrictSerializer(serializers.ModelSerializer):
#     district=DistrictSerializer(read_only=False)
#     class Meta:
#         model=SubDistrict
#         fields="__all__"

# class WardSerializer(serializers.ModelSerializer):
#     # subdistrict=SubDistrictSerializer(read_only=False)
#     class Meta:
#         model=Ward
#         fields='__all__'

class FeatureListingSerializer(serializers.ModelSerializer):
    location = DistrictSerializer(many=False)
    class Meta:
        model= Listing
        fields='__all__'

