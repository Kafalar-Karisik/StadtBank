"""Django Module(s)"""
from django.contrib import admin

# Register your models here.
from .models import Customer, Action

admin.site.register(Customer)
admin.site.register(Action)
