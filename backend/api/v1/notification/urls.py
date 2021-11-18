from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (NotificationList,)

app_name = "notification"

urlpatterns = [
    path('notifications/', NotificationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
