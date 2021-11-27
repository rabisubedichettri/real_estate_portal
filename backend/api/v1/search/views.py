from rest_framework.decorators import api_view
from rest_framework import status
from listing.models import Listing
from api.v1.tools.paginator import customPagination
from . import  serializers
# custom response format
from api.v1.ResponseFormat import responseFormat

@api_view(['GET'])
def featureView(request):
    """
    this featured view can be accessed  by anyone
    """
    page_number=request.GET.get('page_number',1)
    page_size=request.GET.get('page_size',5)
    results=Listing.objects.filter(featured=True,active=True)
    data=customPagination(Serializers=serializers.FeatureListingSerializer,
                     queryset=results,
                     page_number=page_number,
                     page_size=page_size)
    return responseFormat(
        status="success",
        message="successfully fetched",
        data=data,
        status_code=status.HTTP_200_OK
    )



def randomView():
    pass

def recentView():
    pass

# based on pervious behaviour
def predictView():
    pass

def mostView():
    pass

def favouriteView():
    pass

def searchFormView():
    pass

def searchMapView():
    pass

# gettting all details related to instance
def detailView():
    pass


def allViewOnce():
    pass

