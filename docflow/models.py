from datetime import datetime

from django.core.validators import MinLengthValidator
# from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User

from .validators import validate_file_extension


class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    level = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.level


class Document(models.Model):
    document = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])

    def __str__(self):
        return self.document.name


class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Комментарий {self.author} от {self.created_date}'


class Application(models.Model):
    current_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    student_last_name = models.CharField(max_length=100)
    student_first_name = models.CharField(max_length=100)
    student_father_name = models.CharField(max_length=100, null=True, blank=True)

    student_passport = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    student_education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    student_id_number = models.CharField(max_length=50, null=True, blank=True)
    student_group_number = models.CharField(max_length=50, null=True, blank=True)

    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True, blank=True)

    created_date = models.DateTimeField(default=datetime.now, editable=False)
    last_change_date = models.DateTimeField(default=datetime.now)
    last_change_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # убрать blank=True, если пользователя можно определять при создании заявки

    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True)

    is_archived = models.BooleanField(default=False)

    def __str__(self):
        student_full_name = f'{self.student_last_name} {self.student_first_name}'
        if self.student_father_name is not None:
            student_full_name += f' {self.student_father_name}'
        return f'Заявка {student_full_name} от {self.created_date.date()}'


# TODO добавить юзеру новые поля по гайдам GPT
class UserTest(models.Model):
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    is_admin = models.BooleanField(default=False)
