from listing.models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from django.core.files.base import ContentFile
import base64
import six
import uuid
User = get_user_model()

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PropertyType
        fields='__all__'


class PropertyTypeUpdateSerializer(serializers.ModelSerializer):
    pk=serializers.IntegerField(max_value=9999999999, min_value=1)
    class Meta:
        model=PropertyType
        fields='__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Amenity
        fields='__all__'

class AmenityUpdateSerializer(serializers.ModelSerializer):
    pk=serializers.IntegerField(max_value=9999999999, min_value=1)
    class Meta:
        model=Amenity
        fields='__all__'

# new

class AmenityTypePostSerializer(serializers.ModelSerializer):

    class Meta:
        model=AmenityType
        fields='__all__'


class AmenityTypeUpdateSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(max_value=9999999999, min_value=1)
    class Meta:
        model = AmenityType
        fields = '__all__'

class AmenityTypeSerializer(serializers.ModelSerializer):
    amenity=AmenitySerializer(many=True,read_only=True)
    class Meta:
        model = AmenityType
        fields = ['amenity']


class SingleListingSerializer(GeoFeatureModelSerializer):
    profile_image=Base64ImageField(max_length=None,
        use_url=True,
        required=False,
        allow_null=True,
        allow_empty_file=True)
    class Meta:
        model = Listing
        fields = ['profile_image',
                  'purpose','phone_number','property_id',
                  'categories','title','description',
                  'direction','active','featured',
                  'built_year','cost','land_area',
                  'road_size','geo_location','video_link',
                  'user','type','location','id'
                  ]
        geo_field="geo_location"

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'





