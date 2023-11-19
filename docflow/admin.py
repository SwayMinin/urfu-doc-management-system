from django.contrib import admin
from .models import Department, EducationLevel, Application

for model in [Department, EducationLevel, Application]:
    admin.site.register(model)
