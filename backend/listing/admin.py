
from .models import *

from django.contrib.gis import admin

admin.site.register(PropertyType)
admin.site.register(Amenity)
admin.site.register(AmenityType)


@admin.register(Listing)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    pass