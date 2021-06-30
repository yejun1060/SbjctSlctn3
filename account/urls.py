from django.urls import path
from . import views


urlpatterns = [
    path("login.do", views.login, name="login"),
]