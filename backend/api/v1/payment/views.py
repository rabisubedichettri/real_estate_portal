import json
from api.v1.ResponseFormat import responseFormat
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from pricing.models import UserCart
from django.db.models import F
import requests
from django.conf import settings
from api.v1.pricing.serializers import UserCartSerializer
from pricing.models import  UserCart,TotalBill,PackageBill,PaidPackageInfo,UsercartSnapShort
import json
from django.utils import timezone
def getCartData(user):
    objects = UserCart.objects.filter(user=user).annotate(
        result=F('quantity') * F('package__price'))
    if objects.exists:
        sum = 0
        for i in objects:
            sum += i.result
        return sum
    else:
        return 0

def getSnapshot(user):
    objects=UserCart.objects.filter(user=user)
    data=UserCartSerializer(objects,many=True).data
    return data



@api_view(['POST'])
def khaltiInit(request):
    if request.user.is_authenticated:
   
        sum = getCartData(request.user)
        if sum != 0:

            #delete old snapshot if present
            old_snapshot=UsercartSnapShort.objects.filter(user=request.user)
            old_snapshot.delete()

            #create new  snapshot
            snapshot=UsercartSnapShort.objects.create(
                user=request.user,
                data=getSnapshot(request.user)
            )
            snapshot.save()


            payload = {
                'public_key':settings.KHALTI_PUBLIC_KEY,
                "mobile": request.POST.get('mobile'),
                'paymentPreference': request.POST.get('paymentPreference','KHALTI'),
                'transaction_pin': request.POST.get('transaction_pin'),
                'amount': sum*100,
                'product_identity': snapshot.id,
                'product_name': request.POST.get('cart',"cart")
            }

            headers = {
            "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
             }

            try:
                response = requests.post(settings.KHALTI_INITIATE_URL,payload,headers=headers)
               
                if response.status_code == 200 :
                    snapshot.token=response.json()['token']
                    snapshot.save()
                    return responseFormat(
                    status="success",
                    message="check your confirmation code",
                    data=response.json(),
                    status_code=status.HTTP_200_OK)
                else:
                    print(response.json())
                    return responseFormat(
                    status="fail",
                    message="your payment can not proceed",
                    data=response.json(),
                    status_code=status.HTTP_400_BAD_REQUEST)

                   
            except request.exceptions.HTTPError as e:
                return responseFormat(
                    status="fail",
                    message="internal error",
                    data=response.json(),
                    status_code=status.HTTP_400_BAD_REQUEST)

        else:
            return responseFormat(
                status="fail",
                message="You do not have any package in cart",
                status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return responseFormat(status="fail",
                              message="unauthorized",
                              status_code=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def khaltiConfirm(request):
    if request.user.is_authenticated:
        try:
            # Get snapshot from db
            token=request.POST.get('token')
           
            snapshot=UsercartSnapShort.objects.get(token=token,user=request.user)
            # Get current snapshot 
            if snapshot.data==getSnapshot(request.user):
                payload = {
                "token": token,
                'transaction_pin': request.POST.get('transaction_pin'),
                'confirmation_code':request.POST.get('confirmation_code'),
                'public_key':settings.KHALTI_PUBLIC_KEY,
                }

                headers = {
                "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
                    }

                try:
                    response = requests.post(settings.KHALTI_CONFIRM_URL,payload,headers=headers)
                    if response.status_code == 200 :
                        # transfer cart to database
                        cart_instance=UserCart.objects.filter(user=request.user)
                        if cart_instance.exists():
                            data=response.json()
                            totalBill_instance=TotalBill.objects.create(
                                user=request.user,
                                payment_method='Khalti',
                                transaction_id=data['idx'],
                                total_cost=data['amount']/100,
                                token=data['token'],
                                mobile=data['mobile'],
                                product_identity=data['product_identity']

                            )
                            totalBill_instance.save()
                            for instance in cart_instance:
                                temp1 = PackageBill.objects.create(
                                    package=instance.package,
                                    price=instance.package.price,
                                    quantity=instance.quantity,
                                )
                                temp1.save()
                                for quantity in range(instance.quantity):
                                    expired_time=timezone.now()+timezone.timedelta(days=instance.package.duration_month * 30)
                                    temp2=PaidPackageInfo.objects.create(
                                        package=temp1,
                                        remaining_items=instance.package.items,
                                        expired_at=expired_time
                                    )
                                    temp2.save()
                            cart_instance.delete()
                            snapshot.delete()
                             # database tra
                            return responseFormat(
                            status="success",
                            message="Payment has been Successful",
                            data=response.json(),
                            status_code=status.HTTP_200_OK)
                        else:
                            return responseFormat(status="fail",
                                                        message='your cart is empty, you have to add some package and then do',
                                                        status_code=status.HTTP_406_NOT_ACCEPTABLE)
                       
                    else:
                        print(response.json())
                        return responseFormat(
                        status="fail",
                        message="Payment has been fail",
                        data=response.json(),
                        status_code=status.HTTP_400_BAD_REQUEST)

                        
                except request.exceptions.HTTPError as e:
                    return responseFormat(
                        status="fail",
                        message="internal error",
                        data=response.json(),
                        status_code=status.HTTP_400_BAD_REQUEST)

                
       
        except:
            return responseFormat(status="fail",
                              message="unauthorized",
                              status_code=status.HTTP_401_UNAUTHORIZED)
    else:
       
        return responseFormat(status="fail",
                                message="unauthorized",
                                status_code=status.HTTP_401_UNAUTHORIZED)



        
        





