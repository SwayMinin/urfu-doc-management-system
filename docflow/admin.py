from django.contrib import admin
from . import models

for model in [models.Department, models.Course, models.StudyLevel, models.Application, models.Comment, models.Document]:
    admin.site.register(model)
