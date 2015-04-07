# -*- coding: utf-8 -*-

from django.contrib import admin
from dcc_colab.models import User, Course, Topic, Test, TopicContent, TestContent

class UserAdmin(admin.ModelAdmin):
    fields = ['facebook_id', 'name', 'type']

class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'professors']

class TopicAdmin(admin.ModelAdmin):
    fields = ['name', 'course']
    list_display = ['name', 'course']

admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
