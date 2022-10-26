# ORM Prisma with Python


## Requirements

* Prisma ORM
* Prisma Client Python

## Install Prisma ORM
Installing Prisma Client Python

```
$ pip install -U prisma
```

## Config Prisma schema
Generating Prisma Client Python

```
$ prisma db push
```

Downloading binaries  [####################################]  100%                                
Prisma schema loaded from schema.prisma
Datasource "db": SQLite database "database.db" at "file:database.db"

SQLite database database.db created at file:database.db

🚀  Your database is now in sync with your schema. Done in 22ms

✔ Generated Prisma Client Python (v0.7.0) to 
3.9.14/envs/venv_prisma_3.9.14/lib/python3.9/site-packages/prisma in 266ms

## Running application

```
$ python main.py
```

## SQLite Databases

* [Documentation](https://www.sqlite.org/index.html)
* [FAQ](https://www.sqlite.org/faq.html)
* [Command Line Shell](https://sqlite.org/cli.html)

### Connection SQLite

```
$ sqlite3 database.db
sqlite>
```

### Show tables

```
$ sqlite> .tables
Post  User
```

### Describe table

```
$sqlite> .schema User
CREATE TABLE IF NOT EXISTS "User" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "email" TEXT NOT NULL,
    "name" TEXT
);
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");
```