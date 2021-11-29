from account.models import User
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Local imports
from location.models import Ward
from .choices import (Property_Status, PropertyType_CHOICES, AmenityType_CHOICES, PROPERTY_PURPOSE,
                      PROPERTY_DIRECTION, PROPERTY_CATEGORY)
from .utils import photo_path
from .validators import validate_image

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PropertyType(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.CharField(max_length=200, help_text='for example : house,shop,room,apartment')
    icon = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, choices=PropertyType_CHOICES, default='u',)
    suggested_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
 

    def __str__(self):
        return str(self.id)


class Amenity(models.Model):
    name = models.CharField(max_length=15, unique=True)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, choices=AmenityType_CHOICES)
    suggested_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Amenities"


    def __str__(self):
        return str(self.id)


class AmenityType(models.Model):
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE,related_name="amenity")
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=AmenityType_CHOICES, default='u')
    suggested_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)

class ListingManger(models.Manager):
    def detailView(self,request, id):
        result = self.filter(id=id, active=True)
        if request.user.is_authenticated and not request.user.is_admin and request.user.is_active:
            if result.exists():
                ip=get_client_ip(request)
                check_counter=CountPropertyView.objects.filter(ip__exact=ip,listing_id=id).exists()
                if not check_counter:
                    new_counter=CountPropertyView.objects.create(ip=ip,listing_id=id)
                    new_counter.save()
                check_recent=RecenltyPropertyView.objects.filter(user=request.user,listing_id=id).order_by('-created_at')
                if not check_recent.exists():
                    if check_recent[0].listing.id!=id:
                        new_recent = RecenltyPropertyView.objects.create(user=request.user, listing_id=id)
                        new_recent.save()
        return result


class Listing(models.Model):
    purpose = models.CharField(choices=PROPERTY_PURPOSE, max_length=1)
    phone_number = models.CharField(max_length=15)
    property_id = models.CharField(max_length=10, null=True, blank=True)
    categories = models.CharField(max_length=1, choices=PROPERTY_CATEGORY)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=4000)
    direction = models.CharField(max_length=2, choices=PROPERTY_DIRECTION)
    active = models.BooleanField(default=False)  # expiration of listing
    featured = models.BooleanField(default=False)
    publish_at = models.DateTimeField(null=True, blank=True)  # if not publish then draft
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    built_year = models.PositiveSmallIntegerField()
    cost=models.DecimalField(max_digits=10, decimal_places=3)

    status = models.CharField(choices=Property_Status, max_length=1, default='D')  # sold or did not sell
    land_area = models.DecimalField(max_digits=10, decimal_places=3)
    road_size = models.DecimalField(max_digits=10, decimal_places=3)
    location = models.ForeignKey(Ward, on_delete=models.CASCADE)
    tole = models.CharField(max_length=15, null=True, blank=True)
    geo_location = models.PointField(null=True,blank=True)  # {"type":"Point","coordinates":[114.65554242776489,1796.270164701642]}
    video_link = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to="images/listing/", null=True,blank=True,validators=[validate_image])
    objects = ListingManger()
    def __str__(self):
        return str(self.title)




    class Meta:
        ordering=['-created_at']


class PropertyAmenity(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amenity_type = models.ForeignKey(AmenityType, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()  # number of amenity

    class Meta:
        verbose_name_plural = 'Property Amenities'
        unique_together = ("listing", "amenity_type")

    def __str__(self):
        return str(self.id) or 'Null'


class PropertyRating(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    star = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.star)


class PropertyComment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        default=None,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='parent_%(class)s',
        verbose_name='parent comment'
    )

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-created_date']


class UpdateProperty(Listing):
    orginal_post = models.OneToOneField(Listing, related_name="update_listing", on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class PropertyImages(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=photo_path, validators=[validate_image])

    def __str__(self):
        return str(self.id)


class FavouriteProperty(models.Model):
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class CountPropertyView(models.Model):
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)
    ip=models.GenericIPAddressField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class RecenltyPropertyView(models.Model):
    listing=models.ForeignKey(Listing,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    class Meta:
        ordering=['created_at']


