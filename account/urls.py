from django.urls import path
from . import views


urlpatterns = [
    path("login.do", views.user_login, name="login"),
    path("teacher-login.do", views.teacher_login, name="teacher-login"),
    path("logout.do", views.logout, name="logout"),
]