from django.db import models
from  basetables.base import BaseModel
# Create your models here.
# from courses.models import Course
class OrganizationCategory(BaseModel):
    name = models.CharField(verbose_name='机构类别',max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机构类别'
        verbose_name_plural = verbose_name

class City(BaseModel):
    city = models.CharField(verbose_name='城市',max_length=20)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

class Organization(BaseModel):
    name = models.CharField(verbose_name='机构名字',max_length=20)
    image = models.ImageField(verbose_name='机构图片',max_length=200)
    organizationcategory = models.ForeignKey(OrganizationCategory,verbose_name='机构类别',on_delete=models.CASCADE)
    city = models.ForeignKey(City,verbose_name='城市',on_delete=models.CASCADE)
    teacher_num = models.IntegerField(default=0,verbose_name='教师数量')
    course_num = models.IntegerField(default=0,verbose_name='课程数目')
    learn_num = models.IntegerField(default=0,verbose_name='学习人数')
    detail_addr = models.CharField(max_length=200,verbose_name='详细地址',blank=True,null=True)
    introduce = models.TextField(verbose_name='机构介绍')
    recommend_num = models.IntegerField(verbose_name='推荐指数')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name

class Teacher(BaseModel):
    name = models.CharField(verbose_name='教师名字',max_length=20)
    image = models.ImageField(upload_to='teacher/%y/%m/%d',verbose_name='头像')
    work_time = models.IntegerField(verbose_name='工作年数',default=0)
    organization = models.ForeignKey(Organization,verbose_name='所在公司',on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='年龄',default=0)
    postion = models.CharField(verbose_name='职位',max_length=20,blank=True,null=True)
    characteristic = models.CharField(verbose_name='教学特色',max_length=20,blank=True,null=True)
    course_num = models.IntegerField(default=0,verbose_name='课程数')
    learn_num = models.IntegerField(default=0,verbose_name='学习人数')
    gender = models.BooleanField(verbose_name='性别',choices=((True,'男'),(False,'女')),default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name




# class GoodCourse(BaseModel):
#     course = models.ForeignKey(courses.Course,verbose_name='课程',on_delete=models.CASCADE)
#     organization = models.ForeignKey(Organization,verbose_name='机构',on_delete=models.CASCADE)



