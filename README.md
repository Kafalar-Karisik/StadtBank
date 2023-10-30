# StadtBank

[![Pylint](https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml/badge.svg)](https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml)

## Setup

### Create Environment (Optional)

To create a virtual environment, run the following command:

```shell
python -m venv .venv
python -m pip install -r requirements.txt
```

## Create Database

To set up the database, perform the following steps:

1. Generate migration files:

```shell
python manage.py makemigrations Actions
python manage.py makemigrations Customers
```

2. Apply the migrations:

```shell
python manage.py migrate
```

## Data Samples

You can use the bin/randCus.py script to generate sample data in the db.sqlite3 database.

## Data Tables

Here are the SQL definitions for the database tables:

### Actions Table

```sql

CREATE TABLE "actions" (
    "id"           integer PRIMARY KEY AUTOINCREMENT,
    "nr"           integer NOT NULL,
    "datum"        datetime NOT NULL,
    "actiontype"   text NOT NULL,
    "amount"       real NOT NULL,
    "related_nr"   real
);
```

### Customers Table

```sql

CREATE TABLE "customers" (
    "nr"     integer PRIMARY KEY NOT NULL,
    "name"   text NOT NULL,
    "saldo"  real NOT NULL
);
```

## Admin GUI

To access the admin GUI, you need to create a superuser account first. Run the following command:

```shell

python manage.py createsuperuser
```

Note: Please ensure that your database migrations are applied before running the `createsuperuser` command.
