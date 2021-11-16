from django.urls import path
from .views import (districtView,provienceView,subdistrictView,wardView)
app_name="location"
urlpatterns = [
 path("provience/", provienceView, name="provience"),
 path("district/<int:id>/provience/",districtView,name="district"),
 path("provience/<int:id>/subdistrict/",subdistrictView,name="subdistrict"),
 path("subdistrict/<int:id>/ward/",wardView,name="ward"),
]

