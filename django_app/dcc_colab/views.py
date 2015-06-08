# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from dcc_colab.models import *


def index(request):

    template = loader.get_template('dcc_colab/index.html')
    context = RequestContext(request, {
    })

    return HttpResponse(template.render(context))

@login_required(login_url='/')
def home(request):

    template = loader.get_template('dcc_colab/home.html')
    context = RequestContext(request, {
        'menu_home': 'active'
    })

    return HttpResponse(template.render(context))

@login_required(login_url='/')
def courses(request):

    courses = Course.objects.all()

    template = loader.get_template('dcc_colab/courses.html')
    context = RequestContext(request, {
        'courses' : courses,
        'menu_courses': 'active',
    })

    return HttpResponse(template.render(context))

@login_required(login_url='/')
def course(request):

    course_id = request.GET.get('id')

    if course_id is not None:
        course = Course.objects.get(id=course_id)
        template = loader.get_template('dcc_colab/course.html')
        context = RequestContext(request, {
            'course' : course,
            'menu_courses': 'active',
        })
        return HttpResponse(template.render(context))
