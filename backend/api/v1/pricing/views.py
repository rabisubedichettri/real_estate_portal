from django.shortcuts import render
from django.db.models import Q
from api.v1.tools.paginator import customPagination
# serializers imports
from django.utils import timezone

from django.db import IntegrityError, transaction
from django.conf import settings
from .serializers import PricingSerializer, UserCartSerializer, PostCartSerializer

# rest_frameworks imports
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# model imports
from pricing.models import Pricing, UserCart,TotalBill,PackageBill,PaidPackageInfo
from django.contrib.auth.decorators import login_required

# custom response format
from api.v1.ResponseFormat import responseFormat


class PricingList(APIView):

    
    def get(self, request, format=None):

        queryset = Pricing.objects.filter(active=True)
        deserializer = PricingSerializer(queryset, many=True)
        return responseFormat(status="success",
                              message="successfully fetched",
                              data=deserializer.data,
                              status_code=status.HTTP_200_OK)

def actionCartQuantity(action,cart_instance):
    if action=='increase':
        cart_instance.quantity+=1
        cart_instance.save()
        return "increase"
    else:
        if cart_instance.quantity==1:
            cart_instance.delete()
            return "delete"
        else:
            cart_instance.quantity-=1
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
                package_id=serializer.validated_data['package']
                instance=UserCart.objects.filter(package=package_id,user=request.user)
                if instance.exists():
                    actionCartQuantity(action="increase",cart_instance=instance[0])

                    packageName = instance[0].package.name
                    return responseFormat(status="success",
                                        message=f"increased 1 more quantity to package {packageName}".format(packageName),
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
          
        else:return responseFormat(status="fail",
                                message="unauthrozied",
                                status_code=status.HTTP_401_UNAUTHORIZED)


class UserCartView(APIView):
    
    def delete(self, request, id,format=None,*args, **kwargs):
         if request.user.is_authenticated:
        
            try:
                instance=UserCart.objects.get(pk=id,user=request.user)
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



    def put(self, request,id, format=None):
        if request.user.is_authenticated:
            action = request.GET.get('action', False)
            if action in ['increase', 'decrease']:
                try:
                    instance = UserCart.objects.get(pk=id,user=request.user)
                    result=actionCartQuantity(action=action, cart_instance=instance)
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





