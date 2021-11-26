from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Pricing)
admin.site.register(models.UserCart)
admin.site.register(models.TotalBill)
admin.site.register(models.PackageBill)
admin.site.register(models.PaidPackageInfo)
admin.site.register(models.UsercartSnapShort)
