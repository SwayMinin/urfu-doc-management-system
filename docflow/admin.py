from django.contrib import admin

from .models import *

for model in [Department, Course, StudyLevel, Application, Comment, Document, Profile]:
    admin.site.register(model)
