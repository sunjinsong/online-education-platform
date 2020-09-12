# Generated by Django 3.1 on 2020-09-11 08:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('name', models.CharField(max_length=30, verbose_name='章节名字')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('image', models.ImageField(upload_to='course/%y/%m/%d', verbose_name='课程封面')),
                ('time', models.IntegerField(default=0, verbose_name='课程时长')),
                ('learn_num', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_num', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('grade', models.IntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], default=1, verbose_name='难度等级')),
                ('introduce', models.CharField(max_length=200, verbose_name='简介')),
                ('chapter_num', models.IntegerField(default=0, verbose_name='章节数目')),
                ('course_category', models.CharField(max_length=20, verbose_name='课程类别')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('should_kown', models.CharField(max_length=200, verbose_name='课程须知')),
                ('learn_kg', models.CharField(max_length=200, verbose_name='能学到什么')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.teacher', verbose_name='授课老师')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('name', models.CharField(max_length=20, verbose_name='视频名字')),
                ('time', models.IntegerField(default=0, verbose_name='视频时长')),
                ('url', models.URLField(verbose_name='视频url')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.chapter', verbose_name='所属章节')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('file', models.FileField(upload_to='resource/%y/%m/%d', verbose_name='课程资源')),
                ('name', models.CharField(max_length=20, verbose_name='资源名字')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='所属课程')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='所属课程'),
        ),
    ]