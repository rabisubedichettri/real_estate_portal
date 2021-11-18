# rest_framework imports
from rest_framework import serializers

# model imports
from notification.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notification
        fields='__all__'