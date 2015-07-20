# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_consume',
            field=models.IntegerField(max_length=3, verbose_name=b'\xe5\x91\xa8\xe5\xad\xa6\xe6\x97\xb6'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(max_length=200, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe7\xae\x80\xe4\xbb\x8b'),
        ),
    ]
