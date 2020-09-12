from django.db import models
from basetables.base import BaseModel
# Create your models here.

class SlideShowTop(BaseModel):
    image = models.ImageField(verbose_name='显示图片',upload_to='slideshowtop')
    url = models.URLField(verbose_name='链接地址',max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = '主页上部轮播图'
        verbose_name_plural = verbose_name


class SlideShowBottom(BaseModel):
    image = models.ImageField(verbose_name='显示图片', upload_to='slideshowbottom')
    url = models.URLField(verbose_name='链接地址', max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = '主页中部轮播图'
        verbose_name_plural = verbose_name