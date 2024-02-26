from django.contrib import admin

from .models import Action, Customer

# Register your models here.

admin.site.register([Action, Customer])
