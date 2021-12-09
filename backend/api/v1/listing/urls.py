from django.urls import path, include
from .views import *

app_name = "listing"
urlpatterns = [
    path("property-type/", propertyTypeView),
    path("amenity/", AmenityView),
    path("amenity-type/", AmenityTypeView),  # Create
    path("amenity-type/<int:id>", SingleAmenityTypeView),  # delete,update,read
    path("listings/", listingView),
    path("listings/<int:id>/", singleListingView),
    path("drafts/", ListDraftView.as_view()),
    path("drafts/<int:id>/", DeatailDraftview.as_view()),
    path("<int:id>/rate/", RateView.as_view()),
    path("rating/<int:id>/average/", averageRating),
    path("comments/<int:id>", CommnetView.as_view())

]
