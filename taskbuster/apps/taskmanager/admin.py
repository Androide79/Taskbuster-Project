# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models
 

class ProjectsInLine(admin.TabularInline):
    model = models.Project
    extra = 0

class TagsInLine(admin.TabularInline):
    model = models.Tag
    extra = 0
    
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
 
    list_display = ("username", "interaction", "_projects")
 
    search_fields = ["user__username"]
 
    inlines = [
        ProjectsInLine, TagsInLine
    ]
 
    def _projects(self, obj):
        return obj.projects.all().count()
 
    def _tags(self, obj):
        return obj.tags.all().count()