from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from mooc.models import Course
from django.http import Http404
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
