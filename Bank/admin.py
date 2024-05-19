"""Bank/models.py"""
from django.contrib import admin

from .models import Action, Customer, Setting

admin.site.register([Action, Customer, Setting])
