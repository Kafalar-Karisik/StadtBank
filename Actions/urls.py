from django.urls import path

from . import views

urlpatterns = [
    path('customers/', views.Customers.as_view(), name='kunden_list'),
    path("customers/<int:nr>/", views.CustomerDV.as_view(), name="detail"),
    path('actions/', views.Actions.as_view(), name='action_list'),
    path('pay-in/',views.payIn),
    path('pay-out/', views.payOut),
]