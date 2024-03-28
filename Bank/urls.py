"""Bank/urls.py"""
from django.urls import path

from . import views

app_name = "Bank"
urlpatterns = [
    path("", views.index, name="index"),
    path("customers/", views.Customers.as_view()),
    path("customers/<int:nr>", views.CustomerDV.as_view()),
    path("pay", views.Pay.as_view(), name="Pay In/Out"),
    path("paying", views.pay, name="pay"),
    path("transfer", views.transfer, name="transfer"),
    path("credit", views.Credit.as_view(), name="Credit System")
]
