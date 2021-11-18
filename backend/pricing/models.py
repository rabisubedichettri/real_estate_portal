from django.db import models
import uuid
from account.models import User


# Create your models here.
class Pricing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, unique=True)
    items = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    feature = models.JSONField()
    description = models.TextField()
    duration_month = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)


class UserCart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    package = models.ForeignKey(Pricing, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class TotalBill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.id)


class PackageBill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(Pricing, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_bill = models.ForeignKey(TotalBill, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)


class PaidPackageInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(PackageBill, on_delete=models.SET_NULL, null=True)
    remaining_items = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return str(self.id)
