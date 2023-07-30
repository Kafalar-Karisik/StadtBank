# StadtBank

## A basic Bank system with Django and Database

### Data Samples

All Of the Customer Datas in the `customer` table in [`db.sqlite3`](db.sqlite3) are Random created with [`bin/randCus.py`](bin/randCus.py)

### Admin GUI

#### Change it

Username: ``admin``
Password: ``pass``

### Data Forms

```sql
CREATE TABLE "actions" (
    "id"    integer NOT NULL,
    "nr"    integer NOT NULL,
    "datum" datetime NOT NULL,
    "actiontype"    text NOT NULL,
    "amount"    real NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
```

```sql
CREATE TABLE "customers" (
    "nr"    integer NOT NULL,
    "name"  text NOT NULL,
    "saldo" real NOT NULL,
    PRIMARY KEY("nr")
);
```
