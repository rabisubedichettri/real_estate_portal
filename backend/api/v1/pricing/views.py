from django.shortcuts import render
from django.db.models import Q
from api.v1.tools.paginator import customPagination
# serializers imports
from django.utils import timezone
from datetime import datetime
from django.db import DatabaseError, transaction

from django.db import IntegrityError, transaction
from django.conf import settings
from rest_framework.decorators import api_view
from .serializers import UsePackageSerializer, PostPricingSerializer,PricingSerializer,PaidPackageSerializer, UserCartSerializer, PostCartSerializer

# rest_frameworks imports
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# model imports
from pricing.models import Pricing, UserCart, TotalBill, PackageBill, PaidPackageInfo
from django.contrib.auth.decorators import login_required

# custom response format
from api.v1.ResponseFormat import responseFormat
from listing.models import PaidPackageInfo,DraftPackage,Listing

class PricingList(APIView):

    def get(self, request, format=None):
        queryset = Pricing.objects.filter(active=True)
        deserializer = PricingSerializer(queryset, many=True)
        return responseFormat(status="success",
                              message="successfully fetched",
                              data=deserializer.data,
                              status_code=status.HTTP_200_OK)
    def post(self,request):
        if request.user.is_authenticated and request.user.is_admin:
            serializer=PostPricingSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return responseFormat(
                    message="successfully added but needs to be activated for use",
                    status="success",
                    status_code=status.HTTP_200_OK,
                )
            else:
                return responseFormat(
                    message="invalid format in form",
                    status="fail",
                    status_code=status.HTTP_406_NOT_ACCEPTABLE,
                    errors=serializer.errors
                )
        else:
            return responseFormat(
                message="unauthorized",
                status_code=status.HTTP_401_UNAUTHORIZED,
                status="fail"
            )

class PricingDetail(APIView):
    def get(self, request, id,format=None):
        print("myquery: ",request.query_params)
        queryset = Pricing.objects.filter(active=True)
        deserializer = PricingSerializer(queryset, many=True)
        return responseFormat(status="success",
                              message="successfully fetched",
                              data=deserializer.data,
                              status_code=status.HTTP_200_OK)
    def put(self, request,id):
        if request.user.is_authenticated and request.user.is_admin:
            try:
                get_package=Pricing.objects.get(pk=id)
                serializer = PostPricingSerializer(get_package,data=request.POST)
                if serializer.is_valid():
                    serializer.save()
                    return responseFormat(
                        message="updated successfully",
                        status="success",
                        status_code=status.HTTP_200_OK,
                    )
                else:
                    return responseFormat(
                        message="invalid format in form",
                        status="fail",
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        errors=serializer.errors
                    )
            except:
                return responseFormat(
                    message="pricing does not found",
                    status_code=status.HTTP_406_NOT_ACCEPTABLE,
                    status="success"
                )

        else:
            return responseFormat(
                message="unauthorized",
                status_code=status.HTTP_401_UNAUTHORIZED,
                status="fail"
            )
    def delete(self, request):
        pricing_id = request.GET.get("pricing_id", None)
        if request.user.is_authenticated and request.user.is_admin:
            if pricing_id:
                try:
                    get_object = Pricing.objects.get(pk=pricing_id)
                    get_object.delete()
                    return responseFormat(
                        message="successfully deleted",
                        status_code=status.HTTP_200_OK,
                        status="success"
                    )
                except:
                    return responseFormat(
                        message="pricing id does not found",
                        status_code=status.HTTP_400_BAD_REQUEST,
                        status="fail"
                    )

            else:
                return responseFormat(
                    message="you should provide pricing_id",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    status="fail"
                )


        else:
            return responseFormat(
                status="fail",
                message="unauthorized",
                status_code=status.HTTP_401_UNAUTHORIZED
            )

def actionCartQuantity(action, cart_instance):
    if action == 'increase':
        cart_instance.quantity += 1
        cart_instance.save()
        return "increase"
    else:
        if cart_instance.quantity == 1:
            cart_instance.delete()
            return "delete"
        else:
            cart_instance.quantity -= 1
            cart_instance.save()
            return "decrease"


class UserCartViewList(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated:
            queryset = UserCart.objects.filter(user=request.user)
            deserializer = UserCartSerializer(queryset, many=True)
            return responseFormat(status="success",
                                  message="successfully fetched",
                                  data=deserializer.data,
                                  status_code=status.HTTP_200_OK)
        else:
            return responseFormat(status="fail",
                                  message="unauthrozied",
                                  status_code=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        if request.user.is_authenticated:
            serializer = PostCartSerializer(data=request.POST)

            if serializer.is_valid():
                package_id = serializer.validated_data['package']
                instance = UserCart.objects.filter(package=package_id, user=request.user)
                if instance.exists():
                    actionCartQuantity(action="increase", cart_instance=instance[0])

                    packageName = instance[0].package.name
                    return responseFormat(status="success",
                                          message=f"increased 1 more quantity to package {packageName}".format(
                                              packageName),
                                          status_code=status.HTTP_200_OK)
                else:
                    obj = UserCart.objects.create(package=serializer.validated_data['package'], user=request.user)
                    obj.save()
                return responseFormat(status="success",
                                      message="successfully added",
                                      status_code=status.HTTP_200_OK)
            else:
                return responseFormat(status="fail",
                                      message="error in form",
                                      data=serializer.data,
                                      status_code=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return responseFormat(status="fail",
                                  message="unauthrozied",
                                  status_code=status.HTTP_401_UNAUTHORIZED)


class UserCartView(APIView):

    def delete(self, request, id, format=None, *args, **kwargs):
        if request.user.is_authenticated:

            try:
                instance = UserCart.objects.get(pk=id, user=request.user)
                instance.delete()
                return responseFormat(status="success",
                                      message="successfully deleted",
                                      status_code=status.HTTP_200_OK)
            except:
                return responseFormat(status="fail",
                                      message="no package found in your cart",
                                      status_code=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return responseFormat(status="fail",
                                  message="unauthrozied",
                                  status_code=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, id, format=None):
        if request.user.is_authenticated:
            action = request.GET.get('action', False)
            if action in ['increase', 'decrease']:
                try:
                    instance = UserCart.objects.get(pk=id, user=request.user)
                    result = actionCartQuantity(action=action, cart_instance=instance)
                    return responseFormat(status="success",
                                          message=f"successfully {action}d".format(result),
                                          status_code=status.HTTP_200_OK)
                except:
                    return responseFormat(status="fail",
                                          message="package not found",
                                          status_code=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return responseFormat(status="fail",
                                  message="unauthorized ",
                                  status_code=status.HTTP_401_UNAUTHORIZED)


class UserPaidPackageListView(APIView):
    def get(self, request):
        user = request.GET.get("user", "client")
        page_number = request.GET.get("page_number", 1)
        page_size = request.GET.get("page_size", 5)
        type = request.GET.get("type", "active")
        user_id = request.GET.get("user_id", None)
        if request.user.is_authenticated:
            q_object = Q()
            if type == "active":
                q_object.add(Q(expired_at__gte = datetime.now()), Q.AND)
                q_object.add(Q(active=True), Q.AND)
            if type == "deactivate":
                q_object.add(Q(expired_at__lt=datetime.now()), Q.AND)
                q_object.add(Q(active=False), Q.AND)
            # if other type comes then it will select all both active and deactive package
            if user == "admin" and request.user.is_admin:  # for admin
                if isinstance(user_id,int):
                    # check user existence
                    try:
                        get_user=User.objecs.get(pk=user_id)
                        q_object.add(Q(package__total_bill__user=get_user), Q.AND)
                    except:
                        return responseFormat(
                            message="user does not found",
                            status='fail',
                            status_code=status.HTTP_400_BAD_REQUEST
                        )

                # if user is not provided in query then it will select all

            else:  # for client
                q_object.add(Q(package__total_bill__user=request.user), Q.AND)

            # query to database
            results=PaidPackageInfo.objects.filter(q_object)
            data= customPagination(
                page_size=page_size,
                page_number=page_number,
                queryset=results,
                Serializers=PaidPackageSerializer

            )
            return responseFormat(
                message="feteched successfully",
                status='success',
                status_code=status.HTTP_200_OK,
                data=data
,
            )

        else:
            return responseFormat(
                message="unauthorized",
                status='fail',
                status_code=status.HTTP_401_UNAUTHORIZED
            )


# package transcation
@api_view(['POST'])
def UsePackage(request):
    if request.user.is_authenticated:
        seralizer=UsePackageSerializer(request.POST)
        if seralizer.is_valid():
            draft_id=seralizer.validated_data['draft_id']
            package_id=seralizer.validated_data['package_id']
            try:
                with transaction.atomic():
                    get_draft=DraftPackage.objects.get(id=draft_id,user=request.user)
                    get_package=PaidPackageInfo.objects.get(id=package_id,
                                                            package__total_bill__user=request.user,
                                                            remaining_items__gte=1
                                                            )
                    # decrease by 1
                    get_package.remaining_items=get_package.remaining_items-1
                    get_package.save()

                    # copy  item from draft to listing model
                    new_listing = Listing.objects.create(
                        purpose=get_draft.purpose,
                        phone_number=get_draft.phone_number,
                        property_id=get_draft.property_id,
                        categories=get_draft.categories,
                        user=request.user,
                        type=get_draft.type,
                        title=get_draft.title,
                        description=get_draft.description,
                        direction=get_draft.direction,
                        active=True,
                        created_at=get_draft.created_at,
                        built_year=get_draft.built_year,
                        cost=get_draft.cost,
                        status=get_draft.status,
                        land_area=get_draft.land_area,
                        road_size=get_draft.road_size,
                        location=get_draft.location,
                        tole=get_draft.tole,
                        geo_location=get_draft.geo_location,
                        video_link=get_draft.video_link,
                        profile_image=get_draft.profile_image,
                        paid_package=get_package

                    )
                    new_listing.save()
                    get_draft.delete()
                    return responseFormat(
                        message="successfully activated",
                        status_code=status.HTTP_200_OK,
                        status="success"
                    )

            except:
                return responseFormat(
                    message="invalid operation",
                    status_code=status.HTTP_406_NOT_ACCEPTABLE,
                    status="fail"
                )

        else:
            return responseFormat(
                message="inappropirate format",
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                status="fail"
            )

    else:
        return  responseFormat(
            message="unauthorized",
            status_code=status.HTTP_401_UNAUTHORIZED,
            status="fail"
        )


