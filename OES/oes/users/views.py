from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import RegisterForm,ForgetPwdForm
from .models import UserProfile
from utils.sendemail import SendRegisterInfo
from django.db.models import Q
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.conf import settings
# Imaginary function to handle an uploaded file.
import sys
import os

def UserLogin(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if not all([username,password]):        #不能为空
            msg = '信息不完整'
            context={
                'msg':msg,
            }
            return render(request,'login.html',context=context)
        userlist=UserProfile.objects.filter(Q(email=username)|Q(phone=username))
        if not userlist:
            msg = '用户不存在'
            context={
                'msg':msg,
            }
            return render(request,'login.html',context=context)

        user=userlist[0]
        username=user.username
        user=authenticate(username=username, password=password)     #
        if user:    #表示验证成功
            if not user.is_active:      #表示没有激活
                SendRegisterInfo(user)  #发送激活链接
                return HttpResponse('已经发送激活链接到你的邮箱')
            login(request,user)
            return redirect('index:index')
        else:
            msg = '密码错误'
            context = {
                'msg': msg,
            }
            return render(request, 'login.html', context=context)
        # if userlist[0].password != password:


        # if userlist[0].is_active():
        #     msg = '账户没有激活'
        #     context={
        #         'msg':msg,
        #     }
        #     return render(request,'login.html',context=context)
        # login(request,userlist[0])


def UserRegister(request):
    registerform = RegisterForm()
    if request.method == 'GET':

        context={
            'registerform':registerform,
        }
        return render(request,'register.html',context=context)
    else:
        formdata = RegisterForm(request.POST)
        if formdata.is_valid():     #表示输入合法
            email = formdata.cleaned_data['email']
            password = formdata.cleaned_data['password']
            emial_list=UserProfile.objects.filter(email=email)
            if emial_list:      #表示已经存在注册的emial
                msg = 'emial已经被注册'
                context = {
                    'msg': msg,
                    'registerform': registerform,
                }
            else:
                user=UserProfile.objects.create_user(username=email,email=email,password=password)
                user.is_active=0
                user.save()
                SendRegisterInfo(user)
                return HttpResponse('register success')
        else:
            msg='输入不合理'
            context={
                'msg':msg,
                'registerform': registerform,
            }
        return render(request,'register.html',context=context)


def Active_Acount(request,user_id):
    user_list=UserProfile.objects.filter(id=user_id)
    if user_list:
        user_list[0].is_active=1
        user_list[0].save()
        return HttpResponse('激活成功')
    else:
        return HttpResponse('出错')


def ForgetPwd(request):

    if request.method == 'GET':
        form = ForgetPwdForm()
        context={
            'captcha':form,
        }
        return render(request,'forgetpwd.html',context=context)
    else:
        email = request.POST.get('email','')
        if not email:
            context={
                'msg':'不存在这个账户'
            }
            return render(request,'forgetpwd.html',context=context)
        form = ForgetPwdForm(request.POST)
        if not form.is_valid(): #判断是否有效
            context={
                'msg':'输入错误'
            }
            return render(request,'forgetpwd.html',context=context)


@login_required
def UploadHeader(request):
    user = request.user
    with open(str(user.email)+'.png', 'wb') as destination:
        for chunk in request.FILES['file'].chunks():
            destination.write(chunk)

    user.image = '/static/media/header/'+str(user.email)+'.png'
    user.save()
    return redirect('users:usercenterinfo')

@login_required
def UserCenterInfo(request):
    user = request.user         #得到登录的用户
    if request.method == 'GET':
        context={
            'username' : user.username,
            'birthday' : user.birthday,
            'gender' :  user.gender,
            'address' : user.address,
            'phone' : user.phone,
            'email' : user.email,
            'image' : user.image,
        }
        return render(request,'user/usercenter-info.html',context=context)
    else:
        username = request.POST['nick_name']
        birthday = request.POST['birday']
        gender = request.POST['gender']
        address = request.POST['address']
        phone = request.POST['mobile']
        print('hfdfd')
        user.username = username
        user.birthday = birthday
        user.gender = gender
        user.address = address
        user.phone = phone

        user.save()

        return redirect('users:usercenterinfo')

@login_required
def ResetPwd(request):
    user = request.user
    if request.method == 'GET':
        return HttpResponse('error')
    else:
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        if pwd1 != pwd2:
            return HttpResponse('密码不一致')
        user.set_password(pwd2)

        user.save()
        logout(request)
        return redirect('users:login')


@login_required
def UserFavCourse(request):
    if request.method == 'GET':
        return render(request,'user/usercenter-fav-course.html')


@login_required
def UserFavTeacher(request):
    if request.method == 'GET':
        return render(request,'user/usercenter-fav-teacher.html')

@login_required
def UserFavOrg(request):
    if request.method == 'GET':
        return render(request,'user/usercenter-fav-org.html')

@login_required
def MyMsg(request):
    if request.method == 'GET':
        return render(request,'user/usercenter-message.html')

@login_required
def MyCourse(request):
    if request.method == 'GET':
        return render(request,'user/usercenter-mycourse.html')


@login_required
def UserLogout(request):
    logout(request)
    return redirect('index:index')