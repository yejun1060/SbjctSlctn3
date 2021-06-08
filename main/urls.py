from django.urls import path
from . import views


urlpatterns = [
    path("1", views.signUp, name='sign_up'),
    path("2", views.signIn, name="sign_in"),
    path("3", views.singInCheck, name="sign_in_back"),
]