"""Django Module(s)"""
from django.urls import path

from . import views

urlpatterns = [
    path('customers/', views.Customers.as_view(), name='kunden_list'),
    path("customers/<int:nr>/", views.CustomerDV.as_view(), name="customer_detail"),
    path('actions/', views.Actions.as_view(), name='action_list'),
    path("actions/<int:id>/", views.ActionDV.as_view(), name="action_detail"),
    path('pay-in/',views.pay_in),
    path('pay-out/', views.pay_out),
    path('settings/', views.Settings.as_view())
]
