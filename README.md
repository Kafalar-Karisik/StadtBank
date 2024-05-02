# StadtBank

[![Pylint](https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml/badge.svg?branch=Django-Tailwind)](https://github.com/Kafalar-Karisik/StadtBank/actions/workflows/pylint.yml)

[Documents](https://kafalar-karisik.github.io/StadtBank/)

Basic Bank System with Web GUI and database

## Setup

### Create Environment (Optional)

To create a virtual environment, run the following command:

#### Activate virtual environment (for Unix-based systems)

```shell
python -m venv .venv
source .venv/bin/activate
```

#### Activate virtual environment (for Windows)

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

To set up the database, perform the following step:

- Show up to migration files:

  ```shell
  python manage.py migrate
  ```

## Data Samples

You can use the [bin/randCus.py](bin/randCus.py) and [bin/randAct.py](bin/randAct.py) for generating sample data for your database.

## Running Server

After all setup, you can run the program with:

```shell
python manage.py runserver
```

> Use `--insecure` if you can't get Static Files

## Admin GUI

To access the admin GUI, you need to create a superuser account first. Run the following command:

```shell
python manage.py createsuperuser
```

> or you can run [bin/userSetup.py](bin/userSetup.py) for Account Setup

For access, you need to go to `http://IP_ADDRESS/admin`

> **Note:** Please ensure that your database migrations are applied before running the `createsuperuser` command.
