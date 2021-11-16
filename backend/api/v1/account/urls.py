from django.urls import path
from .views import (ManageUser,ChangeUserPassword,updateUserInfo)
app_name="account"
urlpatterns = [
    path("",ManageUser,name="manage_user"),
    path("password/",ChangeUserPassword,name="change_password"),
    path("info/",updateUserInfo,name="update_user_info")
]

