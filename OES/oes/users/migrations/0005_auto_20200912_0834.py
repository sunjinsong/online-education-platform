# Generated by Django 3.1 on 2020-09-12 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200912_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.BooleanField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别'),
        ),
    ]