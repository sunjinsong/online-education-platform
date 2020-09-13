from django.db import models

# Create your models here.
from basetables.base import BaseModel
from organizations.models import Teacher,Organization
from courses.models import Course
from users.models import UserProfile

class FavThing(BaseModel):
    favtype = models.IntegerField(verbose_name='收藏的类型',choices=((1,'收藏课程'),(2,'收藏老师'),(3,'收藏机构')))
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    favid = models.IntegerField(verbose_name='收藏课程or机构or老师的id')