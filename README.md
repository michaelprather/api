# ToDo Demo

## Purpose

Prototype a basic RESTful API using Python and Django Rest Framework.

## Endpoints

| Method | Endpoint                   | Description
| ------ | -------------------------- | -----------
| GET    | `/todos/`                  | Fetches the entire list of todos
| GET    | `/todos/?completed=<value>`| Fetches a list of completed todos
| GET    | `/todos/?search=<q>`       | Fetches todos with tasks containing the provided phrase
| POST   | `/todos/`                  | Creates a todo
| PATCH  | `/todos/<pk>/`             | Updates a todo
| DELETE | `/todos/<pk>/`             | Deletes a todo

## Getting started

1. Clone this Github repo in your IDE of choice
2. Create a virtual environment
   ```shell
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install project dependencies
   ```shell
   pip install -r requirements.txt
   ```
4. Create and initialize the database
   ```shell
   python manage.py migrate
   ```

## How to run the development server locally

```shell
python manage.py runserver
```

## How to run tests

```shell
python manage.py test
```

## How to access Django Admin

1. Create a superuser
   ```shell
   python manage.py createsuperuser
   ```
2. Start the development server (see instructions above)
3. Go to `http://127.0.0.1:8000/admin/` in your browser and login using the superuser credentials created during Step 1.

## Liberties taken because this project is not intended for production

1. The Django secret key is hard-coded rather than being stored as an environment variable outside of version control. 
2. The default SQLite database was used in lieu of Postgres or another more robust database management system.
3. Endpoints are unprotected and all todos are shared as if only a single User would interact with this API.

*Note: This list is not comprehensive.*
