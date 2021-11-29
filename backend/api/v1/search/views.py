from rest_framework.decorators import api_view
from rest_framework import status
from listing.models import Listing,FavouriteProperty,RecenltyPropertyView,CountPropertyView
from api.v1.tools.paginator import customPagination
from . import  serializers
# custom response format
from api.v1.ResponseFormat import responseFormat
from django.db import models

@api_view(['GET'])
def ShortView(request):
    """
    this featured view can be accessed by anyone
    """
    view=request.GET.get('view','feature')
    page_number=request.GET.get('page_number',1)
    page_size=request.GET.get('page_size',5)

    if view=="most":

        results = (CountPropertyView.objects
                   .filter(listing__active=True)
                   .annotate(dcount=models.Count('listing'))
                   .order_by('dcount')
                   )
        data = customPagination(Serializers=serializers.MostViewSerializer,
                                queryset=results,
                                page_number=page_number,
                                page_size=page_size)
        return responseFormat(
            status="success",
            message="successfully fetched",
            data=data,
            status_code=status.HTTP_200_OK
        )




    # based upon ip for forntend  and user for backend
    elif view=='recent' and request.user.is_authenticated:
        results=(RecenltyPropertyView.objects
                 .filter(user=request.user)
                 .order_by()
                 .distinct('listing__id')
                 )
        print(results.query)
        data = customPagination(Serializers=serializers.RecentViewSerializer,
                                queryset=results,
                                page_number=page_number,
                                page_size=page_size)
        return responseFormat(
            status="success",
            message="successfully fetched",
            data=data,
            status_code=status.HTTP_200_OK
        )





    elif view=='favourite' and request.user.is_authenticated:
        results=FavouriteProperty.objects.filter(user=request.user).order_by('-created_at')

    elif view=='random':
        results=Listing.objects.filter(active=True).order_by('?')

    # #based on pervious behaviour
    # elif view=="predict":
    #     pass

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


@api_view(['GET'])
def LisitingdetailView(request,id):
    results = Listing.objects.detailView(request=request,id=id)
    data = serializers.DetailViewSerializer(results,many=True).data
    return responseFormat(
        status="success",
        message="successfully fetched",
        data=data,
        status_code=status.HTTP_200_OK
    )





