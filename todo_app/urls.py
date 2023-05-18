from django.urls import path

from . import views

urlpatterns = [
    path('', views.tasks , name="home"),
    path('task/<str:pk>/', views.task , name="task"),
    path('create_task/', views.createTask , name="create_task"),
    path('delete_task/<str:pk>/', views.deleteTask , name="delete_task"),
]