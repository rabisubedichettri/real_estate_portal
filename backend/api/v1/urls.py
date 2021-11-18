from django.urls import path, include

app_name = "v1"
urlpatterns = [
    path("accounts/", include("api.v1.account.urls", namespace="account")),
    path("location/", include("api.v1.location.urls", namespace='location')),
    path("listing/", include("api.v1.listing.urls", namespace='listing')),
    path("notification/", include("api.v1.notification.urls", namespace='notification')),
    path("pricing/", include("api.v1.pricing.urls", namespace='pricing')),
]
