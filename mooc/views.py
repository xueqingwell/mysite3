# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from mooc.models import Course
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext
from django import forms
# Create your views here.


@login_required
def mooc_list(request):
    ml = Course.objects.all()
    return render_to_response('mooc_list.html', {'ml': ml})


@login_required
def mooc_detail(request, id):
    try:
        md = Course.objects.get(id=str(id))
    except Course.DoesNotExist:
        raise Http404
    return render_to_response('mooc_detail.html', {'md': md})

#
# @login_required
# def course_setting(request, id, action="add"):
#     course_chose_to_modify = get_object_or_404(CourseUse, id=str(id))
#     go = HttpResponse("success")
#     if action == "add":
#         course_chose_to_modify.save()
#         messages.success(request, "tian_jia_cheng_gong")
#     return HttpResponse("sddsdd")
# class CourseSettingForm(forms.Form):
#     userid = forms.IntegerField(label='userid')
#     classid = forms.IntegerField(label='classid')
#
#
# @login_required
# def course_add(request, id):
#     if request.method == 'POST':
#         course_settting_user = request.user.id
#     else:
#         course_settting_user = None
#     return render_to_response('mooc_detail.html', {'csu': course_settting_user}, content_type=RequestContext(request))


@login_required
def course_add(request, id):
    try:
        user = User.objects.get(id=request.user.id)
        course = Course.objects.get(id=id)
        course.course_choose.add(user)
        course.save()
        messages.success(request, "选课成功")
        return HttpResponseRedirect('/index/')
        # return HttpResponse("success")
    except Course.DoesNotExist:
        raise Http404


@login_required
def course_delete(request, id):
    try:
        user = User.objects.get(id=request.user.id)
        course = Course.objects.get(id=id)
        course.course_choose.remove(user)
        course.save()
        messages.success(request, "退课成功")
        return HttpResponseRedirect('/index/')
    except Course.DoesNotExist:
        raise Http404


@login_required
def show_my_course(request):
    user = User.objects.get(id=request.user.id)
    # course = Course.objects.all()
    # all_course = Course.objects.all()
    my_course = user.course_set.all()
    return render_to_response('mooc_select_show.html', {'my_course': my_course})


@login_required
def show_who_choose_this_class(request, id):
    course = Course.objects.get(id=id)
    class_mates = course.course_choose.all()
    return render_to_response('mooc_class_mates.html', {'class_mates': class_mates})
