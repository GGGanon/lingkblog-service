# LingKBlog API Service

A simple and beautiful blog system, powered by love!!!❤️

## Built With

- [flask](https://github.com/pallets/flask) - The web framework used
- [SQLite](https://sqlite.org/lang.html) - The database used
- RESTful - The design style

## Installation

### Install requirements

```Shell
pip3 install -r requirements.txt
```

### Initialize the database

We use SQLite3 as our database, so you need to install SQLite in your environment.

Use the following commands to manage your database:

```Shell
# Create tables
python3 manage.py db upgrade
``` 

### Run

Then, run and enjoy it!

```Shell
python app.py
```

## To-do List

- [ ] Management API
  - [x] User login
  - [ ] Account system
  - [x] Article system
  - [x] Site configuration
- [ ] Blog API
- [ ] API docs