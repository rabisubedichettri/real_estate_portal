# rest_frameworks imports
from rest_framework.views import APIView
from rest_framework import status

# custom response format
from api.v1.ResponseFormat import responseFormat

class PricingAPIView(APIView):
    def get(self, request, format=None):
        pass


