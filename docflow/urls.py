from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
prefix_viewset = [
    (r'applications', views.ApplicationViewSet),
    (r'departments', views.DepartmentViewSet),
    (r'courses', views.CourseViewSet),
    (r'study-levels', views.StudyLevelViewSet),
    (r'documents', views.DocumentViewSet),
    (r'comments', views.CommentViewSet),
    (r'user-profiles', views.UserProfileViewSet),
    (r'users', views.UserViewSet),
    (r'groups', views.GroupViewSet),
]
for prefix, viewset in prefix_viewset:
    router.register(prefix, viewset)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/documents/<int:pk>/download/', views.DownloadDocumentAPIView.as_view(), name='download-document'),
    path('profile/', views.profile, name='users-profile'),
]
