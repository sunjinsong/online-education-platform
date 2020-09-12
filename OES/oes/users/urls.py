from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.UserRegister,name='register'),
    path('login/',views.UserLogin,name='login'),
    path('active_acount/<int:user_id>',views.Active_Acount,name='active_acount'),
    path('forgetpwd/',views.ForgetPwd,name='forgetpwd'),
    path('usercenterinfo/', views.UserCenterInfo, name='usercenterinfo'),
    path('userfavcourse/', views.UserFavCourse, name='userfavcourse'),
    path('userfavteacher/', views.UserFavTeacher, name='userfavteacher'),
    path('userfavorg/', views.UserFavOrg, name='userfavorg'),
    path('usermymsg/', views.MyMsg, name='usermymsg'),
    path('usermycourse/', views.MyCourse, name='usermycourse'),
    path('userlogout/', views.UserLogout, name='userlogout'),
    path('update/pwd/', views.ResetPwd, name='resetpwd'),
    path('image/upload/', views.UploadHeader, name='uploadheader'),
]