import time

try:
    from django.contrib.auth.models import User
except:
    pass


# curl -X POST http://127.0.0.1/newPass

class TOTPError(Exception):
    pass


# You can customize it with your Super User Account
def newWorkerPassword(adminPass: str):
    """Change Worker password. It will return the new Password"""
    if User.objects.filter(username='admin', is_superuser=True).exists():
        # If there is, prompt for the password
        admin_password = input(
            "Enter the password for the superuser 'admin': ")

        # Retrieve the user with the username "admin"
        admin_user = User.objects.get(username='admin')

        # Check if the provided password is correct
        if admin_user.check_password(admin_password):
            passw = str(int(time.time()))[-5:]
            user = User.objects.get(username="worker")
            user.set_password(passw)
            user.save()
            return passw
        else:
            raise TOTPError("Incorrect password for superuser 'admin'.")
    else:
        raise TOTPError("There is no superuser with the username 'admin'.")


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
    print(newWorkerPassword(input("Enter Admin Password:")))
