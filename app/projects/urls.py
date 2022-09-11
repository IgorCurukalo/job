from django.urls import path
from app.projects.views import EditProject, DeleteProject, AddProject


urlpatterns = [
    #проект
    path('project/new/', AddProject.as_view(), name='addProject'),
    path('project/<int:pk>/edit/', EditProject.as_view(), name='editProject'),
    path('project/<int:pk>/delete/', DeleteProject.as_view(), name='deleteProject'),
    ]