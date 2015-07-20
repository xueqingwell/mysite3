from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from mooc.models import Course, UserProfile
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext

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


@login_required
def mooc_select_show(request):
    my_profile = UserProfile()
    my_course = my_profile.users_course.all()
    my_class_mates = my_profile.course_user.all()
    return render_to_response('mooc_select_show.html', {'my_course': my_course, 'my_class_mate': my_class_mates})

@login_required
def mooc_select_add(request, id):
    my_profile = UserProfile()
    my_profile.save()
    moment_user = request.user
    moment_course = Course.objects.get(id=str(id))
    my_profile.users_course.add(moment_course)
    my_profile.course_user.add(moment_user)
    my_profile.save()
    return render_to_response('mooc_detail.html', content_type=RequestContext(request))
