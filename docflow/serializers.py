from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Application


# TODO добавить поле для POST заявки в апи
class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['url', 'student_last_name', 'student_first_name', 'student_father_name', 'comment']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ['url', 'student_last_name', 'student_first_name', 'student_father_name', 'comment']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
