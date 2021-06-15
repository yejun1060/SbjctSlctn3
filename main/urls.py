from django.urls import path
from . import views


urlpatterns = [
    path("2", views.login, name="login"),
    path("4", views.logout, name='logout'),
    path("5", views.teacher_login, name='teacher_login'),
]