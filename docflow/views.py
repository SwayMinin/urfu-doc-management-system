from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from .models import Application, Comment
from .serializers import ApplicationSerializer, CommentSerializer, UserSerializer, GroupSerializer


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.all().order_by('last_change_date')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('last_change_date')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
