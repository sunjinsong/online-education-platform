# Generated by Django 3.1 on 2020-09-10 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('email', models.CharField(max_length=6, verbose_name='邮件地址')),
                ('emialtype', models.IntegerField(choices=[(1, '注册激活'), (2, '密码找回')], verbose_name='邮件种类')),
                ('userid', models.IntegerField(verbose_name='用户的id')),
                ('content', models.CharField(max_length=6, verbose_name='邮件内容')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
