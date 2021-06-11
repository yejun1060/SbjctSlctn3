from django.urls import path
from . import views


urlpatterns = [
    path("2", views.signIn, name="sign_in"),
    path("3", views.singInCheck, name="sign_in_back"),
    path("4", views.logout, name='logout'),
    path("5", views.teacher_signIn, name='teacher_sign_in'),
]