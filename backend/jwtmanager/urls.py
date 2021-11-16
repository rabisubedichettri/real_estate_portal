from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers#remove later

from .views import checking_token,logout

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view(), name='token_get_access'),
    path('obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', logout, name='auth_logout'),
    path("check/",checking_token),

]

