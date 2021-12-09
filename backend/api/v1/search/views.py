from rest_framework.decorators import api_view
from rest_framework import status
from listing.models import Listing, FavouriteProperty, RecenltyPropertyView, CountPropertyView
from api.v1.tools.paginator import customPagination
from . import serializers
# custom response format
from api.v1.ResponseFormat import responseFormat
from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Difference, Distance

from django.db.models import Q


@api_view(['GET'])
def ShortView(request):
    """
    this featured view can be accessed by anyone
    """
    view = request.GET.get('view', 'feature')
    page_number = request.GET.get('page_number', 1)
    page_size = request.GET.get('page_size', 5)

    if view == "most":

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
    elif view == 'recent' and request.user.is_authenticated:
        results = (RecenltyPropertyView.objects
                   .filter(user=request.user)
                   .order_by()
                   .distinct('listing__id')
                   )
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





    elif view == 'favourite' and request.user.is_authenticated:
        results = FavouriteProperty.objects.filter(user=request.user).order_by('-created_at')

    elif view == 'random':
        results = Listing.objects.filter(active=True).order_by('?')

    # #based on pervious behaviour
    # elif view=="predict":
    #     pass

    else:
        results = Listing.objects.filter(featured=True, active=True)

    data = customPagination(Serializers=serializers.ShortViewSerializer,
                            queryset=results,
                            page_number=page_number,
                            page_size=page_size)
    return responseFormat(
        status="success",
        message="successfully fetched",
        data=data,
        status_code=status.HTTP_200_OK
    )


@api_view(['GET'])
def searchFormView(request):
    try:
        form_query = {
            'purpose': request.GET.get('purpose', 'R'),
            'category': request.GET.get('category', None),
            'type': request.GET.get('type', None),
            'direction': request.GET.get('direction', None),
            'min_cost': request.GET.get('min_cost', None),
            'max_cost': request.GET.get('max_cost', None),
            'status_': request.GET.get('status', None),
            'location': request.GET.get('location', None),

        }
        q_object = Q()
        if form_query['purpose']:
            q_object.add(Q(purpose=form_query['purpose']), Q.AND)

        elif form_query['category']:
            q_object.add(Q(categories=form_query['category']),Q.AND)

        elif form_query['type']:
            print(form_query['type'])
            q_object.add(Q(type=form_query['type']),Q.AND)
        else:
            pass

        # elif form_query['direction']:
        #     query += Q(direction=form_query['direction'])
        # elif form_query['min_cost'] and form_query['max_cost'] :
        #     query += Q(direction=form_query['direction'])
        # elif form_query['status_']:
        #     query += Q(status=form_query['status_'])

        data=Listing.objects.filter(q_object)
        print(data)
        return responseFormat(
            status="success",
            message="successful",
            status_code=status.HTTP_200_OK,
        )

    except:
        return responseFormat(
            status="fail",
            message="unsuccessful",
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
        )


@api_view(['GET'])
def searchMapView(request):
    try:
        x = request.GET.get('latitude')
        y = request.GET.get('longitude')
        distance = request.GET.get('distance')
        base_point = Point(float(x), float(y), srid=4326)
        queries = Listing.objects.all().filter(active=True,
                                               geo_location__distance_lt=(base_point, D(km=distance))
                                               ).annotate(distance=Distance('geo_location', base_point))
        serializer = serializers.MapViewSerializer(queries, many=True)

        return responseFormat(
            status="success",
            message="successfully fetched",
            status_code=status.HTTP_200_OK,
            data=serializer.data
        )
    except:
        return responseFormat(
            status="faill",
            message="unsCcessfull",
            status_code=status.HTTP_400_BAD_REQUEST,
        )


@api_view(['GET'])
def LisitingdetailView(request, id):
    results = Listing.objects.detailView(request=request, id=id)
    data = serializers.DetailViewSerializer(results, many=True).data
    return responseFormat(
        status="success",
        message="successfully fetched",
        data=data,
        status_code=status.HTTP_200_OK
    )
