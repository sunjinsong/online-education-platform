from django.db import models
from datetime import datetime


class BaseModel(models.Model):
    create_time=models.DateTimeField(verbose_name='创建时间',default=datetime.now)

    class Meta:
        abstract = True

