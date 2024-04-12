import time

try:
    from django.contrib.auth.models import User
except:
    pass


# curl -X POST http://127.0.0.1/newPassw


def newWorkerPassword() -> str:
    """Change Worker password with the last 5 character of current timestamp (It is not ONE TIME Password!!!)"""
    passw = str(int(time.time()))[-5:]
    user = User.objects.get(username="worker")
    user.set_password(passw)
    user.save()
    return passw


if __name__ == "__main__":
    import os
    import sys

    import django
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..')))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'StadtBank.settings')
    django.setup()
    from django.contrib.auth.models import User
    print(newWorkerPassword())
