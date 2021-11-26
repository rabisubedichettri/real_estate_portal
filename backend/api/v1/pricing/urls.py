from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PricingList,UserCartView,UserCartViewList
app_name = "pricing"

urlpatterns = [
    path('', PricingList.as_view()),
    path('usercart/', UserCartViewList.as_view()),
    path('usercart/<uuid:id>/', UserCartView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
