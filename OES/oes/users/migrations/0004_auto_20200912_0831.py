# Generated by Django 3.1 on 2020-09-12 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200912_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='male', max_length=10, verbose_name='性别'),
        ),
    ]
