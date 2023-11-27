from django.contrib import admin
from .models import *

for model in [Department, EducationLevel, Application, Comment, Document]:
    admin.site.register(model)
