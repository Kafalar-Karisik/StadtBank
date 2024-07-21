import os
import sys

from getpass import getpass

import django

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'StadtBank.settings')
django.setup()

from django.contrib.auth.models import Group, Permission, User

from TOTP import newWorkerPassword

passw = getpass()

User.objects.create_superuser(
    username="admin", email="", password=passw)

User.objects.create_user("worker", "", "").save()
print(newWorkerPassword(adminPass=passw))

Group_L4 = Group.objects.create(name="Authorized-L4")
Group_L4.permissions.add(
    *Permission.objects.filter(content_type__model='customer'))
Group_L4.permissions.add(
    *Permission.objects.filter(content_type__model='action'))
Group_L4.permissions.add(
    *Permission.objects.filter(content_type__model='credit'))
User.objects.get(username="worker").groups.add(Group_L4)
