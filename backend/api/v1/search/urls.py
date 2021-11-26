from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "search"

urlpatterns = [
    path('recent-view/', views.recentView, name='recent-view'),
    path('feature-view/', views.featureView, name='feature-view'),
    path('most-view/', views.mostView, name="most-view"),
    path('favourite-view/', views.favouriteView, name="favourite-view"),
    path('random-view', views.randomView, name='random-view'),
    path('form-view', views.searchFormView, name='form-view'),
    path('map-view', views.searchMapView, name='map-view', )

]

urlpatterns = format_suffix_patterns(urlpatterns)
