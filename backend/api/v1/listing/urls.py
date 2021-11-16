from django.urls import path, include
from .views import *
app_name="listing"
urlpatterns = [
    path("property-type/",propertyTypeView),
    path("amenity/",AmenityView),
    path("amenity-type/",AmenityTypeView),# Create
    path("amenity-type/<int:id>",SingleAmenityTypeView), # delete,update,read
    path("listings/",listingView),
    path("listings/<int:id>/",singleListingView),

]
