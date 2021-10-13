from django.urls import path
from dbApp import views

urlpatterns = [
    path("", views.homePage, name="homePage"),
    
    path("create-student", views.createStudent, name="create-student"),
    path("update-student/<str:pk>/", views.updateStudent, name="update-student"),
    path("delete-student/<str:pk>/", views.deleteStudent, name="delete-student"),
    path("view-student/<str:pk>", views.viewStudent, name="view-student"),

    path("create-teacher", views.createTeacher, name="create-teacher"),
    path("update-teacher/<str:pk>/", views.updateTeacher, name="update-teacher"),
    path("delete-teacher/<str:pk>/", views.deleteTeacher, name="delete-teacher"),
    #path("view-teacher/<str:pk>", views.viewTeacher, name="view-teacher"),
]