# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0002_auto_20150720_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_consume',
            field=models.IntegerField(verbose_name=b'\xe5\x91\xa8\xe5\xad\xa6\xe6\x97\xb6'),
        ),
    ]
