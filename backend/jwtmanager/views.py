from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes



@api_view(['POST'])
def checking_token(request):
    if request.user.is_authenticated:
        return Response({"message": "YES, user is authicated!"})
    else:
        return Response({"message": "NO ,user is not authicated!"})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.POST.get("refresh_token")
        print(refresh_token)
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(
            data={
            'status':"success",
            "message":"Sucessfully logged out",
              "data":"" ,
             "error":"",
        },
            status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(
            data={
                'status': "fail",
                "message": "incorrect refresh token",
                "data": "",
                "error": "",
            },
            status=status.HTTP_400_BAD_REQUEST)

