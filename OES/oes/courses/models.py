from django.db import models
from  basetables.base import BaseModel
# Create your models here.
from organizations.models import Organization,Teacher

class Course(BaseModel):
    name = models.CharField(verbose_name='课程名称', max_length=20)
    image = models.ImageField(upload_to='course/%y/%m/%d', verbose_name='课程封面')
    time = models.IntegerField(default=0, verbose_name='课程时长')
    learn_num = models.IntegerField(verbose_name='学习人数', default=0)
    fav_num = models.IntegerField(verbose_name='收藏人数', default=0)
    grade = models.IntegerField(verbose_name='难度等级', choices=((1, '初级'), (2, '中级'), (3, '高级')), default=1)
    introduce = models.CharField(verbose_name='简介', max_length=200)
    chapter_num = models.IntegerField(verbose_name='章节数目', default=0)
    course_category = models.CharField(verbose_name='课程类别', max_length=20)
    detail = models.TextField(verbose_name='课程详情')
    teacher = models.ForeignKey(Teacher,verbose_name='授课老师',on_delete=models.CASCADE)
    should_kown = models.CharField(max_length=200,verbose_name='课程须知')
    learn_kg = models.CharField(max_length=200,verbose_name='能学到什么')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

class Chapter(BaseModel):
    name = models.CharField(max_length=30,verbose_name='章节名字')
    course = models.ForeignKey(Course,verbose_name='所属课程',on_delete=models.CASCADE)

class Video(BaseModel):
    name = models.CharField(verbose_name='视频名字',max_length=20)
    time = models.IntegerField(verbose_name='视频时长',default=0)
    url = models.URLField(verbose_name='视频url')
    chapter = models.ForeignKey(Chapter,verbose_name='所属章节',on_delete=models.CASCADE)




class resource(BaseModel):
    file = models.FileField(upload_to='resource/%y/%m/%d',verbose_name='课程资源')
    name = models.CharField(verbose_name='资源名字',max_length=20)
    course = models.ForeignKey(Course,verbose_name='所属课程',on_delete=models.CASCADE)
