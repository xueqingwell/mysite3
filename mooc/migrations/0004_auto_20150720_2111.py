# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mooc', '0003_auto_20150720_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseuse',
            name='Course',
        ),
        migrations.RemoveField(
            model_name='courseuse',
            name='User',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_choose',
        ),
        migrations.AddField(
            model_name='course',
            name='course_choose',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CourseUse',
        ),
    ]
