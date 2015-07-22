# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=50, verbose_name="课程名称")
    course_time = models.DateField(auto_now=False, auto_now_add=False, verbose_name="上课时间")
    INDEX_CHOICES = (
        ('1', '第一节'),
        ('2', '第二节'),
        ('3', '第三节'),
        ('4', '第四节'),
    )
    course_index = models.CharField(max_length=1, choices=INDEX_CHOICES, verbose_name="第几节上课")
    SUBJECT_CHOICES = (
        ('CS', '计算机'),
        ('EE', '电子工程'),
        ('CH', '化学'),
        ('MA', '数学'),
        ('PH', '物理'),
        ('BI', '生物'),
    )
    course_subject = models.CharField(max_length=2, choices=SUBJECT_CHOICES, verbose_name="科目")
    course_description = models.TextField(max_length=200, verbose_name="课程简介")
    course_consume = models.IntegerField(verbose_name="周学时")
    course_choose = models.ManyToManyField(User, blank=True)

    def __unicode__(self):
        return self.course_name

    class Meta:
        ordering = ['-id']
        verbose_name = "慕课"
        verbose_name_plural = "慕课课程"


class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_subject']
