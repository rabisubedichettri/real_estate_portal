
from .models import *

from django.contrib.gis import admin

admin.site.register(PropertyType)
admin.site.register(Amenity)
admin.site.register(AmenityType)
admin.site.register(RecenltyPropertyView)
admin.site.register(CountPropertyView)
admin.site.register(FavouriteProperty)
admin.site.register(PropertyRating)


@admin.register(Listing)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    pass