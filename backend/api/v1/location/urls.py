from django.urls import path
from .views import (districtView,provienceView,subdistrictView,wardView)
app_name="location"
urlpatterns = [
 path("provience/", provienceView, name="provience"),
 path("provience/<int:id>/district/",districtView,name="district"),
 path("district/<int:id>/subdistrict/",subdistrictView,name="subdistrict"),
 path("subdistrict/<int:id>/ward/",wardView,name="ward"),
]

