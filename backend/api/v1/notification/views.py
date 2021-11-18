from django.shortcuts import render
from django.db.models import Q
from api.v1.tools.paginator import customPagination


# serializers imports
from .serializers import NotificationSerializer

# rest_frameworks imports
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# model imports
from notification.models import Notification

# custom response format
from api.v1.ResponseFormat import responseFormat


class NotificationList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user_type = request.GET.get('user', 'user')
        user_id = request.GET.get('user_id', False)
        public = request.GET.get('public', False)
        page_number = request.GET.get('page_number', 1)
        page_size = request.GET.get('page_size', 5)
        if request.user.is_admin == True and user_type == "admin":
            if user_id:
                queryset = Notification.objects.filter(user=user_id)
            if public == 'true':
                queryset = Notification.objects.filter(user__isnull=False)
                print("public : ",queryset)
            if public and user_id:
                queryset = Notification.objects.all()
        else:
            query = (Q(user=request.user) | Q(user__isnull=True)) & Q(active=True)
            queryset = Notification.objects.filter(query)

        data=customPagination(queryset=queryset,page_size=page_size,page_number=page_number,Serializers=NotificationSerializer)
        return responseFormat(data=data, status_code=status.HTTP_200_OK)

