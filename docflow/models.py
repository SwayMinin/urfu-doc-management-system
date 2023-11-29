from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from .validators import validate_file_extension


class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class StudyLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    level = models.ForeignKey(StudyLevel, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()

    def __str__(self):
        return f'{self.level} — {self.number} курс'


class Document(models.Model):
    file = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])
    # если нужно ограничить размер файла https://stackoverflow.com/a/35321718/22996061

    def __str__(self):
        return self.file.name


class Comment(models.Model):
    text = models.TextField()

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        author = self.author if self.author is not None else '[Пользователь удалён]'
        return f'Комментарий {author} от {self.created_date}'


class Application(models.Model):
    current_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    student_last_name = models.CharField(max_length=100)
    student_first_name = models.CharField(max_length=100)
    student_father_name = models.CharField(max_length=100, null=True, blank=True)

    student_passport = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    student_id_number = models.CharField(max_length=50, null=True, blank=True)
    student_group_number = models.CharField(max_length=50, null=True, blank=True)
    student_course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    last_change_date = models.DateTimeField(auto_now=True)
    last_change_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    documents = models.ManyToManyField(Document, blank=True)
    comments = models.ManyToManyField(Comment, blank=True)

    is_archived = models.BooleanField(default=False)

    def __str__(self):
        student_full_name = f'{self.student_last_name} {self.student_first_name}'
        if self.student_father_name is not None:
            student_full_name += f' {self.student_father_name}'
        return f'Заявка {student_full_name} от {self.created_date.date()}'


# TODO добавить юзеру новые поля по гайдам GPT
class UserTest(models.Model):
    login = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    is_admin = models.BooleanField(default=False)
