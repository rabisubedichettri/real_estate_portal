from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (PricingList,PricingDetail,UserCartView,UserCartViewList,
                    UserPaidPackageListView,UsePackage)
app_name = "pricing"

urlpatterns = [
    path('', PricingList.as_view()),
    path('<uuid:id>/',PricingDetail.as_view()),
    path('usercart/', UserCartViewList.as_view()),
    path('usercart/<uuid:id>/', UserCartView.as_view()),
    path('paid-packages/',UserPaidPackageListView.as_view()),
    path('use-package/',UsePackage)

]

urlpatterns = format_suffix_patterns(urlpatterns)
