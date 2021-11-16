from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (ProvienceReadSerializer,DistrictReadSerializer,
SubDistrictReadSerializer,WardReadSeraializer)
from location.models import District,Provience,SubDistrict,Ward


@api_view(['GET'])
def provienceView(request):
    objects=Provience.objects.all()
    print(type(objects))
    return Response(ProvienceReadSerializer(objects,many=True).data)


@api_view(['GET'])
def districtView(request,id):
    queryset=District.objects.filter(provience__id=id)
    return Response(DistrictReadSerializer(queryset,many=True).data)


@api_view(['GET'])
def subdistrictView(request,id):
    queryset=SubDistrict.objects.filter(district__id=id)
    return Response(SubDistrictReadSerializer(queryset,many=True).data)

@api_view(['GET'])
def wardView(request,id):
    queryset=Ward.objects.filter(subdistrict__id=id)
    return Response(WardReadSeraializer(queryset,many=True).data)
