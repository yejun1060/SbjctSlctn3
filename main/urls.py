from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("v/2", views.second, name="second"),
    path("v/3", views.third, name="third"),
]
