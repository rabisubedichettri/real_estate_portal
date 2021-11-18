from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


app_name = "pricing"

urlpatterns = [
    # path('', NotificationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
