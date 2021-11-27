from rest_framework.decorators import api_view
from rest_framework import status
from listing.models import Listing
from api.v1.tools.paginator import customPagination
from . import  serializers
# custom response format
from api.v1.ResponseFormat import responseFormat

@api_view(['GET'])
def ShortView(request):
    """
    this featured view can be accessed by anyone
    """
    view=request.GET.get('view','recent')
    page_number=request.GET.get('page_number',1)
    page_size=request.GET.get('page_size',5)

    if view=="most":
        pass

    # based upon ip for forntend  and user for backend
    elif view=='recent':
        pass

    elif view=='favourite' and request.user.is_authenticated:
        pass

    elif view=='random':
        pass

    #based on pervious behaviour
    elif view=="predict":
        pass

    else:
        results=Listing.objects.filter(featured=True,active=True)
    data=customPagination(Serializers=serializers.ShortViewSerializer,
                     queryset=results,
                     page_number=page_number,
                     page_size=page_size)
    return responseFormat(
        status="success",
        message="successfully fetched",
        data=data,
        status_code=status.HTTP_200_OK
    )



def searchFormView():
    pass

def searchMapView():
    pass

# gettting all details related to instance
@api_view(['GET'])
def LisitingdetailView(request,id):
    results = Listing.objects.filter(id=id,active=True)
    data = serializers.DetailViewSerializer(results,many=True).data
    return responseFormat(
        status="success",
        message="successfully fetched",
        data=data,
        status_code=status.HTTP_200_OK
    )





