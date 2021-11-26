from django.urls import path, include
from . import views
app_name = "payment"
urlpatterns = [
    path("khalti/transaction/init/",views.khaltiInit),
    path("khalti/transaction/confirm/",views.khaltiConfirm),
]
