from rest_framework import serializers
from listing.models import Listing,PropertyType
from location.models import Ward,District,SubDistrict,Provience
from  account.models import User


class ProvienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Provience
        fields='__all__'


class DistrictSerializer(serializers.ModelSerializer):
    provience=ProvienceSerializer(many=False)
    class Meta:
        model=District
        fields="__all__"

class SubDistrictSerializer(serializers.ModelSerializer):
    district=DistrictSerializer(many=False)
    class Meta:
        model=SubDistrict
        fields="__all__"

class WardSerializer(serializers.ModelSerializer):
    subdistrict=SubDistrictSerializer(many=False)
    class Meta:
        model=Ward
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    """
    Dont expose User's password and active
    """
    class Meta:
        model=User
        fields=['id','first_name','last_name','email']

class PropertyTypeSerlizer(serializers.ModelSerializer):
    class Meta:
        model=PropertyType
        fields=['id','name']

class ListingSerializer(serializers.ModelSerializer):
    purpose = serializers.CharField(source='get_purpose_display')
    categories = serializers.CharField(source='get_categories_display')
    direction = serializers.CharField(source='get_direction_display')
    status = serializers.CharField(source='get_status_display')
    type = PropertyTypeSerlizer(many=False)
    user=UserSerializer(many=False)
    location = WardSerializer(many=False)


class ShortViewSerializer(ListingSerializer):
    class Meta:
        model= Listing
        fields=['profile_image','id','purpose','categories','cost','location']

class DetailViewSerializer(ListingSerializer):
    class Meta:
        model=Listing
        fields='__all__'
