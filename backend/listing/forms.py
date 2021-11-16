from django import forms
from django.contrib.gis import forms as gisform
from location.models import District

# Local imports
from .models import PropertyType, Amenity, Listing, PropertyComment
# Local validators
from .validators import validate_selector


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = ['name', 'description', 'icon']


class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ['name', 'description', 'icon']


class AmenityTypeForm(forms.Form):
    property_type = forms.CharField(max_length=15, validators=[validate_selector, ])
    amenity = forms.CharField(max_length=15, validators=[validate_selector, ])
    description = forms.CharField(max_length=2000)


class LandForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all())
    type = forms.ModelChoiceField(queryset=PropertyType.objects.all())

    class Meta:
        model = Listing
        fields = ['purpose', 'phone_number', 'property_id', 'land_area',
                  'categories', 'type', 'title', 'description', 'direction',
                  'built_year', 'cost', 'road_size', 'village', 'ward_no',
                  'tole', 'geo_location', 'video_link', 'profile_image',
                  ]


class HomeForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all())
    type = forms.ModelChoiceField(queryset=PropertyType.objects.all())
    amenity = forms.JSONField()

    class Meta:
        model = Listing
        fields = ['purpose', 'phone_number', 'property_id', 'land_area',
                  'categories', 'type', 'title', 'description', 'direction',
                  'built_year', 'cost', 'road_size', 'village', 'ward_no',
                  'tole', 'geo_location', 'video_link', 'profile_image',
                  ]


class TestListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['geo_location', ]


class CommentPropertyForm(forms.ModelForm):
    listing_id = forms.IntegerField()

    class Meta:
        model = PropertyComment
        fields = ['content', 'listing_id']


class mapSearchForm(gisform.Form):
    geo_location = gisform.PointField()
    distance = gisform.IntegerField()

    class Meta:
        fields = '__all__'


class formSearch(forms.ModelForm):
    # location = forms.ModelChoiceField(queryset=District.objects.all())
    min_cost = forms.IntegerField()
    max_cost = forms.IntegerField()

    class Meta:
        model = Listing
        fields = ['categories', 'purpose','location' ]
