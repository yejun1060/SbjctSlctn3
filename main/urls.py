from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("v/2", views.second, name="second"),
    path("v/2-1", views.second_end, name="second_end"),

    path("v/3", views.third1, name="third1"),
    path("v/3-1", views.third2, name="third2"),
    path("v/3-2", views.third_end, name="third_end"),

    path('t/v/1', views.teacher_view, name="teacher"),
]
