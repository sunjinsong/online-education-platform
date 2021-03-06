# Generated by Django 3.1 on 2020-09-13 01:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FavThing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('favtype', models.IntegerField(choices=[(1, '收藏课程'), (2, '收藏老师'), (3, '收藏机构')], verbose_name='收藏的类型')),
                ('favid', models.IntegerField(verbose_name='收藏课程or机构or老师的id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
