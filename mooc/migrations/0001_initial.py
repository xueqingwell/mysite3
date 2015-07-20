# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('course_time', models.DateField(verbose_name=b'\xe4\xb8\x8a\xe8\xaf\xbe\xe6\x97\xb6\xe9\x97\xb4')),
                ('course_index', models.CharField(max_length=1, verbose_name=b'\xe7\xac\xac\xe5\x87\xa0\xe8\x8a\x82\xe4\xb8\x8a\xe8\xaf\xbe', choices=[(b'1', b'\xe7\xac\xac\xe4\xb8\x80\xe8\x8a\x82'), (b'2', b'\xe7\xac\xac\xe4\xba\x8c\xe8\x8a\x82'), (b'3', b'\xe7\xac\xac\xe4\xb8\x89\xe8\x8a\x82'), (b'4', b'\xe7\xac\xac\xe5\x9b\x9b\xe8\x8a\x82')])),
                ('course_subject', models.CharField(max_length=2, verbose_name=b'\xe7\xa7\x91\xe7\x9b\xae', choices=[(b'CS', b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba'), (b'EE', b'\xe7\x94\xb5\xe5\xad\x90\xe5\xb7\xa5\xe7\xa8\x8b'), (b'CH', b'\xe5\x8c\x96\xe5\xad\xa6'), (b'MA', b'\xe6\x95\xb0\xe5\xad\xa6'), (b'PH', b'\xe7\x89\xa9\xe7\x90\x86'), (b'BI', b'\xe7\x94\x9f\xe7\x89\xa9')])),
                ('course_description', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe7\xae\x80\xe4\xbb\x8b')),
                ('course_consume', models.IntegerField(verbose_name=b'\xe5\x91\xa8\xe5\xad\xa6\xe6\x97\xb6')),
            ],
            options={
                'ordering': ['course_consume'],
                'verbose_name': '\u6155\u8bfe',
                'verbose_name_plural': '\u6155\u8bfe\u8bfe\u7a0b',
            },
        ),
    ]
