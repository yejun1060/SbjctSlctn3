from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("v/2", views.second, name="second"),
    path("v/2-1", views.second_end, name="second_end"),

    path("v/3", views.third, name="third"),
    path("v/3-1", views.third_end, name="third_end"),

    path('t/v/1', views.test, name="test"),
]
