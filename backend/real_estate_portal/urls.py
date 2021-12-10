from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new
schema_view = get_schema_view( # new
openapi.Info(
title="Real Estate Portal API",
default_version="v1",
description="Real Estate Portal API",
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="nabin@real.com"),
license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/",admin.site.urls),
    path("token/",include('jwtmanager.urls')),
    path("api/", include("api.urls", namespace="api")),
    path('swagger/', schema_view.with_ui( # new
'swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui( # new
'redoc', cache_timeout=0), name='schema-redoc'),
]
