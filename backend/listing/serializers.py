# from rest_framework import serializers
#
# from .models import (Amenity, PropertyType,AmenityType)
#
#
# class AmenitySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Amenity
#         fields = ['name']
#
#
# class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PropertyType
#         fields = ['id','name']
#
# class AmenityTypeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=AmenityType
#         fields=['status','property_type','amenity','description','description']
#
