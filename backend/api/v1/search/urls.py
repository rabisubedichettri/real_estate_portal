from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "search"

urlpatterns = [
    path('list/', views.ShortView, name='short-view'),
    path("detail/<int:id>",views.LisitingdetailView,name="listing-detail-viewS"),
    path('form/', views.searchFormView, name='form-view'),
    path('map/', views.searchMapView, name='map-view', )


]

urlpatterns = format_suffix_patterns(urlpatterns)
