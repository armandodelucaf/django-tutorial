# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from social_auth.models import UserSocialAuth


def index(request):

    template = loader.get_template('dcc_colab/index.html')
    context = RequestContext(request, {
    })

    return HttpResponse(template.render(context))

def home(request):
    # import ipdb; ipdb.set_trace()

    template = loader.get_template('dcc_colab/home.html')
    context = RequestContext(request, {
    })

    return HttpResponse(template.render(context))
