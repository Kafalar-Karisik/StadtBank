import os
import sys

import django
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

from bin.TOTP import newWorkerPassword

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'StadtBank.settings')
django.setup()


# User.objects.create_superuser(
#    username="admin", email="", password="password")  # Please Change it

User.objects.create_user("worker", "", "").save()
print(newWorkerPassword())
Group_L4 = Group.objects.create(name="Authorized-L4")
Group_L4.permissions.add(
    [*Permission.objects.filter(content_type__model='customer'), *Permission.objects.filter(content_type__model='actions'), *Permission.objects.filter(content_type__model='credit')])
User.objects.get(username="worker").groups.add(Group_L4)
