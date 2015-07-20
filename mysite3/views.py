from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/', content_type=RequestContext(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/', content_type=RequestContext(request))
    else:
        return render_to_response('login.html', context_instance=RequestContext(request))


def index(request):
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/', content_type=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/', content_type=RequestContext(request))
    else:
        form = UserCreationForm()
    return render_to_response('register.html', locals(), context_instance=RequestContext(request))

