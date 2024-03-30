from django.contrib import admin

from .models import Action, Credit, Customer

# Register your models here.

admin.site.register([Action, Customer, Credit])
