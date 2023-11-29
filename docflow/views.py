import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView
from django.http import FileResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import UpdateUserForm, UpdateProfileForm, LoginForm
from .models import Application, Comment, Document, Department, Course, StudyLevel, User, Profile
from .serializers import (ApplicationSerializer, CommentSerializer, UserSerializer, GroupSerializer,
                          DocumentSerializer, DepartmentSerializer, CourseSerializer, StudyLevelSerializer,
                          UserProfileSerializer)


def index(request):
    response = requests.get('http://127.0.0.1:8000/api')
    data = response.json()
    formatted_data = [{'key': key, 'value': value} for key, value in data.items()]
    return render(request, 'docflow/index.html', {'data': formatted_data})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно изменён')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'docflow/profile.html', {'user_form': user_form, 'profile_form': profile_form})


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
    queryset = Application.objects.filter(is_archived=False).order_by('-last_change_date')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(last_change_user=Profile.objects.filter(user=self.request.user)[0])

    def perform_update(self, serializer):
        serializer.save(last_change_user=Profile.objects.filter(user=self.request.user)[0])


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
    queryset = Comment.objects.all()  # .order_by('created_date')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=Profile.objects.filter(user=self.request.user)[0])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
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
