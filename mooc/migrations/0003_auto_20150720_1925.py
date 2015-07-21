# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mooc', '0002_auto_20150720_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseUse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': '\u9009\u8bfe\u8bb0\u5f55',
                'verbose_name_plural': '\u9009\u8bfe\u8bb0\u5f55',
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='course_user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='users_course',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-id'], 'verbose_name': '\u6155\u8bfe', 'verbose_name_plural': '\u6155\u8bfe\u8bfe\u7a0b'},
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AddField(
            model_name='courseuse',
            name='Course',
            field=models.ForeignKey(to='mooc.Course'),
        ),
        migrations.AddField(
            model_name='courseuse',
            name='User',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='course_choose',
            field=models.ForeignKey(blank=True, to='mooc.CourseUse', null=True),
        ),
    ]
