"""Bank/urls.py"""
from django.urls import path

from . import views

app_name = "Bank"
urlpatterns = [
    path("", views.index, name="index"),
    path("customers/<int:nr>", views.CustomerDV.as_view()),
    path("pay",views.Pay.as_view(), name="Pay In/Out")
]
