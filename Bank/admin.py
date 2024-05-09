"""Bank/models.py"""
from django.contrib import admin

from .models import Action, Credit, Customer, Setting


admin.site.register([Action, Customer, Credit, Setting])
