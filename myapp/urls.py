from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    path('index/<str:username>', views.user_hello, name='user hello'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_details, name='projects details'),
    path('task/', views.task, name='task'),
    path('create_task/', views.create_task, name='create task'),
    path('create_project/', views.create_project, name='create project'),
]


