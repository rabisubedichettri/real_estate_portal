from rest_framework import status
from api.v1.ResponseFormat import responseFormat
from listing.models import *

from listing.models import AmenityType
from .serializers import (PropertyTypeSerializer,PropertyTypeUpdateSerializer,
                          AmenityTypeUpdateSerializer,AmenityTypeSerializer,
                          AmenityTypePostSerializer,AmenitySerializer,
                          SingleListingSerializer,ListingSerializer)
from rest_framework.decorators import api_view

@api_view(["GET","POST","PUT"])
def propertyTypeView(request):
    data=""
    message=""
    status_message=""
    errors = ""

    if request.user.is_authenticated:

        if request.method=='GET':
            object=PropertyType.objects.filter(status="u")
            serializer=PropertyTypeSerializer(object,many=True)
            status_code=status.HTTP_200_OK
            message="Successfully Feteched"
            status_message="success"
            data=serializer.data

        elif request.method=='POST':
            deserializer=PropertyTypeSerializer(data=request.POST)
            if deserializer.is_valid():
                deserializer.save()
                message = "Successfully Posted"
                status_message = "Success"
                status_code = status.HTTP_201_CREATED
            else:
                status_message="fail"
                data=deserializer.data
                message="Errors in Data Sent"
                status_code=status.HTTP_400_BAD_REQUEST
                errors=deserializer.errors
            return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)

        elif request.method=="PUT":
            if request.user.is_admin==True:
                serializer=PropertyTypeUpdateSerializer(data=request.POST)
                if serializer.is_valid():
                    try:
                        obj=PropertyType.objects.get(pk=serializer.validated_data['pk'])
                        obj.name=serializer.validated_data['name']
                        obj.description=serializer.validated_data["description"]
                        # here we need to add other fields too for more complex
                        obj.save()
                        status_message="success"
                        message="Successfully updated"
                        status_code=status.HTTP_200_OK
                    except:
                        message="Can not find Property Type"
                        status_message="fail"
                        data=serializer.data
                        status_code=status.HTTP_400_BAD_REQUEST

                else:
                    data=serializer.data
                    errors=serializer.errors
                    status_message="fail"
                    message="Invalid Data Sent"
                    status_code=status.HTTP_400_BAD_REQUEST

            else:
                status_message="fail"
                message="you have no permission"
                status_code=status.HTTP_401_UNAUTHORIZED

    else:
        status_message="fail"
        message="You should be authenticated"
        status_code=status.HTTP_401_UNAUTHORIZED

    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)


@api_view(["GET", "POST", "PUT"])
def AmenityView(request):
    data = ""
    message = ""
    status_message = ""
    errors = ""

    if request.user.is_authenticated:

        if request.method == 'GET':
            object = Amenity.objects.filter(status="u")
            serializer = AmenitySerializer(object, many=True)
            status_code = status.HTTP_200_OK
            message = "Successfully Feteched"
            status_message = "success"
            data = serializer.data
        elif request.method == 'POST':
            deserializer = AmenitySerializer(data=request.POST)
            if deserializer.is_valid():
                deserializer.save()
                message = "Successfully Posted"
                status_message = "Success"
                status_code = status.HTTP_201_CREATED
            else:
                status_message = "fail"
                data = deserializer.data
                message = "Errors in Data Sent"
                status_code = status.HTTP_400_BAD_REQUEST
                errors = deserializer.errors
            return responseFormat(status=status_message, message=message, data=data, status_code=status_code,
                                  errors=errors)

        elif request.method == "PUT":
            if request.user.is_admin == True:
                serializer = AmenityUpdateSerializer(data=request.POST)
                if serializer.is_valid():
                    try:
                        obj = Amenity.objects.get(pk=serializer.validated_data['pk'])
                        obj.name = serializer.validated_data['name']
                        obj.description = serializer.validated_data["description"]
                        # here we need to add other fields too for more complex
                        obj.save()
                        status_message = "success"
                        message = "Successfully updated"
                        status_code = status.HTTP_200_OK
                    except:
                        message = "Can not find Property Type"
                        status_message = "fail"
                        data = serializer.data
                        status_code = status.HTTP_400_BAD_REQUEST

                else:
                    data = serializer.data
                    errors = serializer.errors
                    status_message = "fail"
                    message = "Invalid Data Sent"
                    status_code = status.HTTP_400_BAD_REQUEST

            else:
                status_message = "fail"
                message = "you have no permission"
                status_code = status.HTTP_401_UNAUTHORIZED

    else:
        status_message = "fail"
        message = "You should be authenticated"
        status_code = status.HTTP_401_UNAUTHORIZED

    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)


@api_view(["GET","POST","PUT"])
def AmenityTypeView(request):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    status_code=status.HTTP_200_OK
    if request.user.is_authenticated:
        if request.method == 'GET':
            object = AmenityType.objects.filter(status="u")
            serializer = AmenityTypeSerializer(object, many=True)
            status_code = status.HTTP_200_OK
            message = "Successfully Feteched"
            status_message = "success"
            data = serializer.data

        elif request.method == 'POST':
            deserializer = AmenityTypeSerializer(data=request.POST)
            if deserializer.is_valid():
                deserializer.save()
                message = "Successfully Posted"
                status_message = "Success"
                status_code = status.HTTP_201_CREATED
            else:
                status_message = "fail"
                data = deserializer.data
                message = "Errors in Data Sent"
                status_code = status.HTTP_400_BAD_REQUEST
                errors = deserializer.errors
            return responseFormat(status=status_message, message=message, data=data, status_code=status_code,
                                  errors=errors)

        elif request.method=="PUT":
            pass
    else:
        status_message = "fail"
        message = "You should be authenticated"
        status_code = status.HTTP_401_UNAUTHORIZED

    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)


@api_view(["GET","PUT"])
def SingleAmenityTypeView(request,id):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    status_code=status.HTTP_200_OK

    if request.user.is_authenticated:
        if request.method == "GET":
            # obj=AmenityType.objects.all()
            obj=AmenityType.AmenityType.objects.filter(property_type__id=id).select_related()
            print()
            print(obj)
            serializer=AmenityTypeSerializer(obj,many=True)
            data=serializer.data
    #         status_code = status.HTTP_200_OK
    #         message = "Successfully Feteched"
    #         status_message = "success"
    #
    #     elif request.method == "POST":
    #         pass
    #
    # else:
    #     pass
    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)

@api_view(["GET"])
def listingView(request):
    queryset=Listing.objects.filter(active=True)
    serializer=ListingSerializer(queryset,many=True)
    return responseFormat(
        data=serializer.data,
        status_code=status.HTTP_200_OK
    )

@api_view(["GET","PUT","POST"])
def singleListingView(request,id):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    status_code=status.HTTP_200_OK
    if request.user.is_authenticated:
        if request.method=="POST":
            serializer=SingleListingSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                status_message="success"
                message="Data fetched Successfully"
            else:
                data = serializer.data
                status_message = "fail"
                message="you have not permission"
        else:
            # data = serializer.data
            # errors = serializer.errors
            status_message = "fail"
            message = "Invalid Data Sent"
            status_code = status.HTTP_400_BAD_REQUEST

    elif request.method=="GET":

        obj=Listing.objects.all()
        print(obj)
        serializer=SingleListingSerializer(obj,many=True)
        print(serializer)
        status_code = status.HTTP_200_OK
        message = "Successfully Feteched"
        status_message = "success"
        data = serializer.data

    elif request.method=="PUT":
        pass
    else:
        status_message = "fail"
        message = "You should be authenticated"
        status_code = status.HTTP_401_UNAUTHORIZED

    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)

