from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('m/', include("account.urls")),
    path('s/', include("survey.urls")),
]
