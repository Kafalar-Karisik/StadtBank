# StadtBank

[![Pylint](https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml/badge.svg?branch=Django-Tailwind)](https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml)

## Setup

### Create Environment (Optional)

To create a virtual environment, run the following command:

```shell
python -m venv .venv
source .venv/bin/activate
```

_or_

```shell
python -m venv .venv
.venv\scripts\activate
```

### Install Requirements

Install the required Python Modules

```shell
python -m pip install -r requirements.txt
```

## Create Database

To set up the database, perform the following steps:

1. Show up to migration files:

   ```shell
   python manage.py migrate
   ```

## Data Samples

You can use the [bin/randCus.py](bin/randCus.py) and [bin/randAct.py](bin/randAct.py) for generate sample data for your database.

## Model Formats

Here are the SQL definitions for the database tables:

### Actions Table

```sql

CREATE TABLE "actions" (
    "id"    integer NOT NULL,
    "nr"    integer NOT NULL,
    "date"  datetime NOT NULL,
    "type"  text NOT NULL,
    "amount"    integer NOT NULL,
    "related_nr"    integer,
    "before"    integer,
    PRIMARY KEY("id")
);
```

### Customers Table

```sql
CREATE TABLE "customers" (
    "nr"    integer NOT NULL,
    "name"  text NOT NULL,
    "balance"   integer NOT NULL,
    PRIMARY KEY("nr")
);
```

## Running Server

After all setup you can run the Program with

```shell
./manage.py runserver
```

_or_

```shell
manage.py runserver
```

## Admin GUI

To access the admin GUI, you need to create a superuser account first. Run the following command:

```shell
python manage.py createsuperuser
```

For access you nedd to go `http://IP_ADRESS/admin`

> **_Note: Please ensure that your database migrations are applied before running the `createsuperuser` command._**
