README
=========

.. image:: https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml/badge.svg?branch=Django-Tailwind
   :target: https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml

Setup
-----

Create Environment (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a virtual environment, run the following command:

.. code-block:: shell

   python -m venv .venv
   source .venv/bin/activate

_or_

.. code-block:: shell

   python -m venv .venv
   .venv\scripts\activate

Install Requirements
~~~~~~~~~~~~~~~~~~~~

Install the required Python Modules:

.. code-block:: shell

   python -m pip install -r requirements.txt

Create Database
~~~~~~~~~~~~~~~

To set up the database, perform the following step:

- Show up to migration files:

.. code-block:: shell

   python manage.py migrate

Data Samples
~~~~~~~~~~~~

You can use the ``bin/randCus.py`` and ``bin/randAct.py`` for generating sample data for your database.

Models
------

Here are the SQL definitions for the database tables:

Customer
~~~~~~~~

.. code-block:: python

   nr = models.IntegerField(primary_key=True, unique=True, auto_created=False)
   name = models.TextField()
   balance = models.IntegerField(default=0)
   credits = models.IntegerField(default=0, null=True)

Action
~~~~~~

.. code-block:: python

   id = models.IntegerField(primary_key=True, auto_created=True)
   customer = models.ForeignKey(Customer, related_name="action_customer", on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now=True)
   type = models.TextField(choices=[('payin', 'Pay In'),
                                    ('payout', 'Pay Out'),
                                    ('transfer', 'Transfer')])
   amount = models.IntegerField(null=True)
   related = models.ForeignKey(Customer, related_name="action_related", on_delete=models.CASCADE, null=True)
   before = models.IntegerField(null=True)

Credit
~~~~~~

.. code-block:: python

   customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
   amount = models.IntegerField()
   date = models.DateTimeField(auto_now_add=True)

Running Server
------

After all setup, you can run the program with:

.. code-block:: shell

   ./manage.py runserver

_or_

.. code-block:: shell

   python manage.py runserver

> Use ``--insecure`` if you can't get Static Files

Admin GUI
------

To access the admin GUI, you need to create a superuser account first. Run the following command:

.. code-block:: shell

   python manage.py createsuperuser

> or you can run ``bin/TOTP.py`` for Account Setup

For access, you need to go to ``http://IP_ADDRESS/admin``

> **Note:** Please ensure that your database migrations are applied before running the `createsuperuser` command.
