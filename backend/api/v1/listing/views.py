from rest_framework import status
from api.v1.ResponseFormat import responseFormat
from listing.models import *
from django.core.exceptions import ObjectDoesNotExist
from listing.models import AmenityType
from .serializers import (PropertyTypeSerializer, PropertyTypeUpdateSerializer,
                          AmenityTypeUpdateSerializer, AmenityTypeSerializer,
                          AmenityTypePostSerializer, AmenitySerializer,
                          SingleListingSerializer, ListingSerializer,
                          DraftDetailSerializer,
                          RatingSeralizer, CommentSerlizer,CommentPostSerlizer)
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.v1.tools.paginator import customPagination
from django.db.models import Avg


@api_view(["GET", "POST", "PUT"])
def propertyTypeView(request):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    if request.method == 'GET':
        object = PropertyType.objects.filter(status="v")
        serializer = PropertyTypeSerializer(object, many=True)
        status_code = status.HTTP_200_OK
        message = "Successfully Feteched"
        status_message = "success"
        data = serializer.data

    # if request.user.is_authenticated:
    #     if request.method=='POST':
    #         deserializer=PropertyTypeSerializer(data=request.POST)
    #         if deserializer.is_valid():
    #             deserializer.save()
    #             message = "Successfully Posted"
    #             status_message = "Success"
    #             status_code = status.HTTP_201_CREATED
    #         else:
    #             status_message="fail"
    #             data=deserializer.data
    #             message="Errors in Data Sent"
    #             status_code=status.HTTP_400_BAD_REQUEST
    #             errors=deserializer.errors
    #         return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)
    #
    #     elif request.method=="PUT":
    #         if request.user.is_admin==True:
    #             serializer=PropertyTypeUpdateSerializer(data=request.POST)
    #             if serializer.is_valid():
    #                 try:
    #                     obj=PropertyType.objects.get(pk=serializer.validated_data['pk'])
    #                     obj.name=serializer.validated_data['name']
    #                     obj.description=serializer.validated_data["description"]
    #                     # here we need to add other fields too for more complex
    #                     obj.save()
    #                     status_message="success"
    #                     message="Successfully updated"
    #                     status_code=status.HTTP_200_OK
    #                 except:
    #                     message="Can not find Property Type"
    #                     status_message="fail"
    #                     data=serializer.data
    #                     status_code=status.HTTP_400_BAD_REQUEST
    #
    #             else:
    #                 data=serializer.data
    #                 errors=serializer.errors
    #                 status_message="fail"
    #                 message="Invalid Data Sent"
    #                 status_code=status.HTTP_400_BAD_REQUEST
    #
    #         else:
    #             status_message="fail"
    #             message="you have no permission"
    #             status_code=status.HTTP_401_UNAUTHORIZED
    #
    # else:
    #     status_message="fail"
    #     message="You should be authenticated"
    #     status_code=status.HTTP_401_UNAUTHORIZED

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


@api_view(["GET", "POST", "PUT"])
def AmenityTypeView(request):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    status_code = status.HTTP_200_OK
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

        elif request.method == "PUT":
            pass
    else:
        status_message = "fail"
        message = "You should be authenticated"
        status_code = status.HTTP_401_UNAUTHORIZED

    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)


@api_view(["GET", "PUT"])
def SingleAmenityTypeView(request, id):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    status_code = status.HTTP_200_OK

    if request.user.is_authenticated:
        if request.method == "GET":
            # obj=AmenityType.objects.all()
            obj = AmenityType.AmenityType.objects.filter(property_type__id=id).select_related()
            print()
            print(obj)
            serializer = AmenityTypeSerializer(obj, many=True)
            data = serializer.data
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
    queryset = Listing.objects.filter(active=True)
    serializer = ListingSerializer(queryset, many=True)
    return responseFormat(
        data=serializer.data,
        status_code=status.HTTP_200_OK
    )


@api_view(["GET", "PUT", "POST"])
def singleListingView(request, id):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    status_code = status.HTTP_200_OK
    if request.user.is_authenticated:
        if request.method == "POST":
            serializer = SingleListingSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                status_message = "success"
                message = "Data fetched Successfully"
            else:
                data = serializer.data
                status_message = "fail"
                message = "you have not permission"
        else:
            # data = serializer.data
            # errors = serializer.errors
            status_message = "fail"
            message = "Invalid Data Sent"
            status_code = status.HTTP_400_BAD_REQUEST

    elif request.method == "GET":

        obj = Listing.objects.all()
        print(obj)
        serializer = SingleListingSerializer(obj, many=True)
        print(serializer)
        status_code = status.HTTP_200_OK
        message = "Successfully Feteched"
        status_message = "success"
        data = serializer.data

    elif request.method == "PUT":
        pass
    else:
        status_message = "fail"
        message = "You should be authenticated"
        status_code = status.HTTP_401_UNAUTHORIZED

    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)


class DeatailDraftview(APIView):
    def get(self, request, id):
        if isinstance(id, int):
            user = request.GET.get('client', 'client')
            if request.user.is_authenticated:
                if (user == "admin" and request.user.is_admin):

                    try:
                        query = DraftPackage.objects.get(pk=id)

                    except ObjectDoesNotExist:
                        return responseFormat(status="fail",
                                              message="not found",
                                              status_code=status.HTTP_400_BAD_REQUEST,
                                              )

                else:  # client
                    try:
                        query = DraftPackage.objects.get(pk=id, user=request.user)

                    except ObjectDoesNotExist:
                        return responseFormat(status="fail",
                                              message="not found",
                                              status_code=status.HTTP_400_BAD_REQUEST,
                                              )
                    serializer = DraftDetailSerializer(query)
                    return responseFormat(status="success",
                                          message="fetched successfully",
                                          status_code=status.HTTP_200_OK,
                                          data=serializer.data
                                          )


            else:
                return responseFormat(status="fail",
                                      message="unauthorized",
                                      status_code=status.HTTP_401_UNAUTHORIZED,
                                      )

    def delete(self, request, id):
        if isinstance(id, int):
            user = request.GET.get('client', 'client')
            if request.user.is_authenticated:
                if (user == "admin" and request.user.is_admin):

                    try:
                        query = DraftPackage.objects.get(pk=id)


                    except ObjectDoesNotExist:
                        return responseFormat(status="fail",
                                              message="not found",
                                              status_code=status.HTTP_400_BAD_REQUEST,
                                              )

                else:  # client
                    try:
                        query = DraftPackage.objects.get(pk=id, user=request.user)

                    except ObjectDoesNotExist:
                        return responseFormat(status="fail",
                                              message="not found",
                                              status_code=status.HTTP_400_BAD_REQUEST,
                                              )
                    query.delete()
                    return responseFormat(status="success",
                                          message="deleted successfully",
                                          status_code=status.HTTP_200_OK,

                                          )


            else:
                return responseFormat(status="fail",
                                      message="unauthorized",
                                      status_code=status.HTTP_401_UNAUTHORIZED,
                                      )


class ListDraftView(APIView):
    def get(self, request):
        user = request.GET.get('client', 'client')
        user_id = request.GET.get('user_id', 'all')
        page_number = request.GET.get("page_number", 1)
        page_size = request.GET.get('page_size', 5)
        if request.user.is_authenticated:
            if (user == "admin" and request.user.is_admin):
                if isinstance(user_id, int):
                    query = DraftPackage.objects.filter(user__id=id)
                else:
                    query = DraftPackage.objects.all()


            else:  # client
                query = DraftPackage.objects.filter(user=request.user)
                data = customPagination(Serializers=DraftDetailSerializer,
                                        queryset=query,
                                        page_number=page_number,
                                        page_size=page_size)
                return responseFormat(
                    status="success",
                    message="successfully fetched",
                    data=data,
                    status_code=status.HTTP_200_OK
                )


        else:
            return responseFormat(status="fail",
                                  message="unauthorized",
                                  status_code=status.HTTP_401_UNAUTHORIZED,
                                  )

    def post(self, request):
        user = request.GET.get('client', 'client')
        user_id = request.GET.get('user_id', 'all')
        if request.user.is_authenticated:
            if (user == "admin" and request.user.is_admin):
                if isinstance(user_id, int):
                    try:
                        get_user = User.objects.get(pk=user_id)
                        serializer = DraftDetailSerializer(get_user)
                        if serializer.is_valid():
                            obj = serializer.save(commit=False)
                            obj.user = get_user
                            obj.save()
                            return responseFormat(
                                status="success",
                                message="successfully fetched",
                                status_code=status.HTTP_200_OK,
                                data=serializer.data
                            )
                    except:
                        return responseFormat(
                            status="fail",
                            message="user does not found",
                            status_code=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return responseFormat(
                        status="fail",
                        message="user_id must be defined ",
                        status_code=status.HTTP_400_BAD_REQUEST
                    )


            else:  # client
                query = DraftPackage.objects.filter(user=request.user)
                data = customPagination(Serializers=DraftDetailSerializer,
                                        queryset=query,
                                        page_number=page_number,
                                        page_size=page_size)
                return responseFormat(
                    status="success",
                    message="successfully fetched",
                    data=data,
                    status_code=status.HTTP_200_OK
                )


        else:
            return responseFormat(status="fail",
                                  message="unauthorized",
                                  status_code=status.HTTP_401_UNAUTHORIZED,
                                  )


class RateView(APIView):
    def post(self, request, id):
        if request.user.is_authenticated:
            try:
                get_listing = Listing.objects.get(pk=id)
                seralizer = RatingSeralizer(data=request.POST)
                if seralizer.is_valid():
                    try:
                        get_star = PropertyRating.objects.get(User=request.user,
                                                              listing=get_listing)
                        get_star.star = seralizer.validated_data['star']
                        get_star.save()
                        return responseFormat(
                            message="updated rating",
                            status="success",
                            status_code=status.HTTP_200_OK,
                        )

                    except:
                        new_star = PropertyRating.objects.create(
                            User=request.user,
                            listing=get_listing,
                            star=seralizer.validated_data['star']
                        )
                        new_star.save()
                        return responseFormat(
                            message="rated",
                            status="success",
                            status_code=status.HTTP_200_OK
                        )
                else:
                    return responseFormat(
                        message="failed to rate",
                        status="fail",
                        errors=seralizer.errors,
                        status_code=status.HTTP_406_NOT_ACCEPTABLE
                    )

            except:
                return responseFormat(
                    message="listing does not find",
                    status="fail",
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        else:
            return responseFormat(
                message="unauthorized",
                status="fail",
                status_code=status.HTTP_401_UNAUTHORIZED
            )

    def get(self, request, id):
        if request.user.is_authenticated:
            try:
                get_listing = Listing.objects.get(pk=id)
                try:
                    get_rating = PropertyRating.objects.get(listing=get_listing, User=request.user)
                    return responseFormat(
                        status="success",
                        message="sucessfully fetched",
                        status_code=status.HTTP_200_OK,
                        data={'star': get_rating.star}
                    )
                except:
                    return responseFormat(
                        status="success",
                        message="sucessfully fetched",
                        status_code=status.HTTP_200_OK,
                        data={'star': 0}
                    )

            except:
                return responseFormat(
                    status="fail",
                    message="listing does not find",
                    status_code=status.HTTP_400_BAD_REQUEST,
                )

        else:
            return responseFormat(
                status="fail",
                message="unauthorized",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )


@api_view(['GET'])
def averageRating(request, id):
    query = PropertyRating.objects.filter(listing__id=id).aggregate(Avg('star'))
    return responseFormat(
        status="success",
        message="fetched successfully",
        status_code=status.HTTP_200_OK,
        data={"average_rating": query['star__avg']}
    )


class CommnetView(APIView):
    def get(self, request, id):
        parent=request.GET.get('parent',None)
        try:
            get_listing = Listing.objects.get(pk=id)
            if parent:
                get_comments = PropertyComment.objects.filter(
                    listing=get_listing, parent__id=parent
                )
            else:
                get_comments = PropertyComment.objects.filter(
                    listing=get_listing, parent__isnull=True
                )
            deserializer = CommentSerlizer(get_comments,many=True)
            return responseFormat(
                status="success",
                message="successfully fetched",
                status_code=status.HTTP_200_OK,
                data=deserializer.data
            )
        except:
            return responseFormat(
                message="unable to find property",
                status="fail",
                status_code=status.HTTP_400_BAD_REQUEST
            )

    def post(self,request,id):
        if request.user.is_authenticated:
            get_listing = Listing.objects.get(pk=id)
            serializer=CommentPostSerlizer(data=request.POST)
            if serializer.is_valid():
                content = serializer.validated_data['content']
                parent=serializer.validated_data['id']
                if parent:
                    parnet_obj=PropertyComment.objects.get(id=parent)
                    new_commnet=PropertyComment.objects.create(
                        user=request.user,
                        listing=get_listing,
                        content=content,
                        parent=parnet_obj
                    )
                else:
                    new_commnet = PropertyComment.objects.create(
                        user=request.user,
                        listing=get_listing,
                        content=content,

                    )
                new_commnet.save()
                return responseFormat(
                    status="success",
                    message="commented successfully",
                    status_code=status.HTTP_200_OK
                )
            else:
                return responseFormat(
                    status="fail",
                    message="invalid formate",
                    status_code=status.HTTP_406_NOT_ACCEPTABLE
                )


        else:
            return responseFormat(
                status="fail",
                message="unauthorized",
                status_code=status.HTTP_401_UNAUTHORIZED
            )