# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mooc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_user', models.ManyToManyField(related_name='course_user', null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(max_length=200, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='users_course',
            field=models.ManyToManyField(related_name='users_course', to='mooc.Course'),
        ),
    ]
