# -*- coding: utf-8 -*-

from django.contrib import admin
from dcc_colab.models import User, Course, Topic, Test, TopicContent, TestContent

class UserAdmin(admin.ModelAdmin):
    fields = ['facebook_id', 'name', 'type']

admin.site.register(User, UserAdmin)
