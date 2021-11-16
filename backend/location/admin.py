from django.contrib import admin

# Register your models here.
from location.models import (Provience,District,SubDistrict,Ward)
admin.site.register(Provience)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Ward)