# >>> I'm working now on other Branch(Django-Version) <<<

## StadtBank
A Basic Bank System for RolePlay Game with Kids :D


```sql
CREATE TABLE "kunden" (
	"nr"	INTEGER,
	"name"	TEXT,
	"saldo"	INTEGER,
	PRIMARY KEY("nr")
);

CREATE TABLE "transaktionen" (
	"id"	INTEGER,
	"nr"	INTEGER,
	"datum"	TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	"transaktionstyp"	TEXT,
	"betrag"	REAL,
	FOREIGN KEY("nr") REFERENCES "kunden"("nr"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
```
