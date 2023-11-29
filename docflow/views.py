from django.contrib.auth.models import User, Group
from django.http import HttpResponse, FileResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Application, Comment, Document, Department, Course, StudyLevel
from .serializers import (ApplicationSerializer, CommentSerializer, UserSerializer, GroupSerializer,
                          DocumentSerializer, DepartmentSerializer, CourseSerializer, StudyLevelSerializer)


def index(request):
    return HttpResponse("Заглавная страница, в разработке.")


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows departments to be created.
    """
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows applications to be viewed or edited.
    """
    queryset = Application.objects.filter(is_archived=False).order_by('last_change_date').reverse()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(last_change_user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(last_change_user=self.request.user)


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows ed levels to be created and assigned.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]


class StudyLevelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows ed levels to be created and assigned.
    """
    queryset = StudyLevel.objects.all()
    serializer_class = StudyLevelSerializer
    permission_classes = [permissions.IsAuthenticated]


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be created and deleted.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]


class DownloadDocumentAPIView(APIView):
    def get(self, request, pk):
        try:
            document = Document.objects.get(pk=pk)
            file_path = document.file.path  # Get the file path
            response = FileResponse(open(file_path, 'rb'), as_attachment=True)
            return response
        except Document.DoesNotExist:
            return Response({"message": "Document not found"}, status=status.HTTP_404_NOT_FOUND)


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be created and assigned.
    """
    queryset = Comment.objects.all().order_by('created_date')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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
