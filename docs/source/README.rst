StadtBank
=========

|Pylint|

`Documents <https://kafalar-karisik.github.io/StadtBank/#>`__

Basic Bank System with Web GUI and database

Setup
-----

Create Environment (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a virtual environment, run the following command:

Activate virtual environment (for Unix-based systems)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   python -m venv .venv
   source .venv/bin/activate

Activate virtual environment (for Windows)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   python -m venv .venv
   .venv\scripts\activate

Install Requirements
~~~~~~~~~~~~~~~~~~~~

Install the required Python Modules

.. code:: shell

   python -m pip install -r requirements.txt

Create Database
---------------

To set up the database, perform the following step:

-  Show up to migration files:

   .. code:: shell

      python manage.py migrate

Data Samples
------------

You can use the `bin/randCus.py <bin/randCus.py>`__ and
`bin/randAct.py <bin/randAct.py>`__ for generating sample data for your
database.

Running Server
--------------

After all setup, you can run the program with:

.. code:: shell

   python manage.py runserver

..

   Use ``--insecure`` if you can’t get Static Files

Admin GUI
---------

To access the admin GUI, you need to create a superuser account first.
Run the following command:

.. code:: shell

   python manage.py createsuperuser

..

   or you can run `bin/userSetup.py <modules/scripts.html#bin.userSetup>`__ for Account Setup

For access, you need to go to ``http://IP_ADDRESS/admin``

   **Note:** Please ensure that your database migrations are applied
   before running the ``createsuperuser`` command.

.. |Pylint| image:: https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml/badge.svg?branch=Django-Tailwind
   :target: https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml
