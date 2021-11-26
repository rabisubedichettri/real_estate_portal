from django.core.validators import MaxValueValidator, MinValueValidator
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
    package = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ]
     )

    def __str__(self):
        return str(self.id)

class UsercartSnapShort(models.Model):
    # product id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    data=models.JSONField()
    token=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.id)


    


class TotalBill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)
    mobile=models.CharField(max_length=15,null=True,blank=True)
    token=models.CharField(max_length=25,null=True,blank=True)
    product_identity=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return str(self.id)


class PackageBill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    package = models.ForeignKey(Pricing, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ]
    )
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
