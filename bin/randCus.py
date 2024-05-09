"""bin/ranCus.py"""
import os
import random
import sys

import django
from faker import Faker


def randCus(stop: int = 0):
    for _ in range(random.randint(25, 75) if stop == 0 else stop):
        first_name = fake.first_name()
        last_name = fake.last_name()
        balance = random.randint(0, 100)

        Customer(name=f"{first_name} {last_name}", balance=balance).save()


if __name__ == "__main__":
    fake = Faker()
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..')))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'StadtBank.settings')
    django.setup()

    from Bank.models import Customer
    randCus()
