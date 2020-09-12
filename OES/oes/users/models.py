from django.db import models
from django.contrib.auth.models import AbstractUser


from basetables.base import BaseModel
# Create your models here.

class UserProfile(AbstractUser):
    image=models.ImageField(verbose_name='用户头像',upload_to='userprofile/%y/%m/%d/',default='default.png',max_length=200)
    birthday=models.CharField(verbose_name='出生日期',blank=True,null=True,max_length=30)
    gender=models.BooleanField(verbose_name='性别',choices=((1,'男'),(2,'女')),default=1)
    address=models.CharField(verbose_name='地址',max_length=200)
    phone=models.CharField(verbose_name='电话号码',max_length=11)

class UserEmail(BaseModel):
    email = models.CharField(max_length=6,verbose_name='邮件地址')
    emialtype = models.IntegerField(verbose_name='邮件种类',choices=((1,'注册激活'),(2,'密码找回')))
    userid = models.IntegerField(verbose_name='用户的id')
    content = models.CharField(verbose_name='邮件内容',max_length=6)

