"""Django Module(s)"""
from django.contrib import admin
from django.urls import include, path

from Bank import views as urls

urlpatterns = [
    path('', urls.index),
    path('', include("Bank.urls")),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),  # DEBUG
]
