"""Bank/models.py"""
from django.contrib import admin

from .models import Action, Credit, Customer


admin.site.register([Action, Customer, Credit])
