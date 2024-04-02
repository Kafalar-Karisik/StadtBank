import os
import sys

import django

sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..')))  # Go to Top dir
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'StadtBank.settings')  # Import Project
django.setup()

try:
    from django.contrib.auth.models import Group, Permission, User
    from django.contrib.contenttypes.models import ContentType

    from bin.TOTP import newWorkerPassword
except:
    exit(-1)


User.objects.create_superuser(
    username="admin", email="", password="password")  # Please Change it

User.objects.create_user("worker", "", "").save()
print(newWorkerPassword())
Group_L4 = Group.objects.create(name="Authorized-L4")
Group_L4.permissions.add(
    *Permission.objects.filter(content_type__model='customer'))
User.objects.get(username="worker").groups.add(Group_L4)
