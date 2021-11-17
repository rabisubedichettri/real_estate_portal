from django.db import models
from account.models import User
from .choices import *


class Notification(models.Model):
    type = models.CharField(max_length=2, choices=NotificationType)
    status = models.CharField(max_length=2, choices=NotificationStatus)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

