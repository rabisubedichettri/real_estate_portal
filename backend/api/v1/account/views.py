from rest_framework import status

from django.contrib.auth.hashers import check_password



from rest_framework.decorators import api_view

from .serializers import (UserRegistrationSerializer, PasswordChangeSerializer
                          ,UserUpdateSerializer)
from api.v1.ResponseFormat import responseFormat
from account.models import User

@api_view(['GET', 'POST', 'PUT'])
def ManageUser(request):
    data = ""
    message = ""
    status_message = ""
    errors = ""
    if not request.user.is_authenticated:
        if request.method == 'GET':
            serializer = UserRegistrationSerializer()
            data = serializer.data
            message = "complete your following form"
            status_code = status.HTTP_200_OK
            status_message = "success"

        if request.method == "POST":
            deserializer = UserRegistrationSerializer(data=request.POST)
            print(deserializer)
            if deserializer.is_valid():
                deserializer.save()
                message = "Your registration is completed"
                status_message = "Success"
                status_code = status.HTTP_201_CREATED
            else:
                errors = deserializer.errors
                data = deserializer.data
                message = "Your registration form is failed"
                status_message = "Fail"
                status_code = status.HTTP_406_NOT_ACCEPTABLE

        if request.method == "PUT":  # this is used for update
            message = "df"
            status_code = status.HTTP_200_OK

    else:
        message = "User is already authenticated and please logout for new user registration"
        status_code = status.HTTP_403_FORBIDDEN
        status_message = "fail"
    return responseFormat(status=status_message, message=message, data=data, status_code=status_code, errors=errors)

def check_user_password(email, password):
    instance = User.objects.filter(email=email)
    if instance:  # checking existing user
        if check_password(password=password, encoded=instance[0].password):  # checking password
            return True
        else:
            return False
    else:
        return False

@api_view(['PUT'])
def ChangeUserPassword(request):
    if request.method == "PUT":
        if request.user.is_authenticated:
            dserializer = PasswordChangeSerializer(data=request.POST)
            if dserializer.is_valid():
                if check_user_password(email=request.user.email, password=dserializer.validated_data['old_password']):
                    user = request.user
                    user.set_password(dserializer.validated_data['password1'])
                    user.save()
                    message = "Password Changed Successfully"
                    return responseFormat(message=message, status="success", status_code=status.HTTP_200_OK)
                else:
                    message = "Invalid old password provided"
                    return responseFormat(message=message, status="fail", status_code=status.HTTP_401_UNAUTHORIZED)

            else:
                return responseFormat(status="fail", errors=dserializer.errors, message="Password Unchanged",
                                      status_code=status.HTTP_401_UNAUTHORIZED)
        else:
            return responseFormat(status='fail', message="You need to be logged in",
                                  status_code=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET','PUT'])
def updateUserInfo(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            data=User.objects.filter(id=request.user.id)[0]
            serializer=UserUpdateSerializer(data)
            return responseFormat(data=serializer.data,
                                  status="success",
                                  status_code=status.HTTP_401_UNAUTHORIZED)
        else:  #put method
            deserializer=UserUpdateSerializer(data=request.POST)
            if deserializer.is_valid():
                user=request.user
                user.first_name = deserializer.validated_data['first_name']
                user.last_name = deserializer.validated_data['last_name']
                user.gender = deserializer.validated_data['gender']
                user.save()
                return responseFormat(status="success",
                                          status_code=status.HTTP_200_OK,
                                          message="User information is updated")
            else:
                return responseFormat(status='fail',
                                      message='Incomplete format or Incorrect Values provided',
                                      status_code=status.HTTP_403_FORBIDDEN,
                                      data=deserializer.data,
                                      errors=deserializer.errors)
    else:
        return responseFormat(message="fail",status_code=status.HTTP_401_UNAUTHORIZED)


