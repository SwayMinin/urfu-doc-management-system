from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Application, Comment, Document, Department, Course, StudyLevel


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['url', 'current_department', 'student_last_name', 'student_first_name', 'student_father_name',
                  'student_passport', 'student_course', 'student_id_number', 'student_group_number',
                  'documents', 'comments', 'is_archived', 'last_change_user', 'last_change_date', 'created_date']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudyLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StudyLevel
        fields = '__all__'


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
