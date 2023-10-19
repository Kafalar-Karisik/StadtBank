"""Django Module(s)"""
from django.contrib import admin
from django.urls import include, path

from Actions import views as urls


urlpatterns = [
    path('', urls.index),
    path('', include("Actions.urls")),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")), #DEBUG
]
