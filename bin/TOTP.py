import datetime

from django.contrib.auth.models import Group, User

# curl -X POST http://127.0.0.1/newPassw


def newWorkerPassword():
    passw = datetime.datetime.now(datetime.UTC).strftime('%H%MZ')
    user = User.objects.get(username="worker")
    user.set_password(datetime.datetime.now(datetime.UTC).strftime('%H%MZ'))
    user.save()
    return passw
