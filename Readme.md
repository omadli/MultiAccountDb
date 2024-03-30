# MultiAccount Database Manager

Database graph: https://drawsql.app/teams/omadli/diagrams/sanjarbek
___

## Features
 - Multi Telegram Accounts database managing
 - Working with telethon
 - Sqlite or PostgreSQL database
 - Accounts, Groups, Channels models
 - Working with command line interface
 - Amazing and powerfull admin site interface

___
<br>

## Installation
The installation process consists of 6 steps:

1) Clone this repo:
```shell
$ git clone https://github.com/omadli/MultiAccountDb
```
2) Creating virtual environment and activate it
In Windows:
```shell
$ pip install virtualenv
$ python -m venv venv
$ .\venv\Scripts\activate
```

In Linux:
```shell
$ python3 -m pip install virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
```

3) Install requirement libraries
```shell
$ pip install -r requirements.txt
```

4) Copy `.env.example` file as named `.env` file:
```shell
$ cp .env.example .env
```

5) Edit your environment variables:
> [!WARNING] 
> API_ID and API_HASH is not work with default values!

6) Migrate and run server or createadmin:
```shell
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
Enjoy :)
___
<br>

## Notes:

### Add account with management command `add_user`:
```shell
$ python manage.py add_user
```

<br>

### Dump django database to json file:
```shell
$ python manage.py dumpdata --natural-foreign --natural-primary --indent 4 > initial_db.json
```

<br>

### Load database from json file:
```shell
$ python manage.py loaddata initial_db.json
```

<br>

___
&copy; Murodillo 2024.
