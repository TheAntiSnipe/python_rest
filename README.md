### This repository contains some basic design pattern work done by me.

Note that these patterns are quite redundant for various reasons considering the scale of the project, and are intended purely for practice.

The application is a RESTful CRUD API served through a container that exposes port 8000. It's built with the help of Flask, with the psycopg2 library being used for DB handling.

The structure is a PostgreSQL Docker container hooked up to a Python image with Flask and Psycopg2 packages installed.

Uses the facade pattern for QueryHandler, along with the subsystem pattern. For the database connection handler, a Borg Singleton is showcased.

Instructions to run:
1. Install Docker
2. `docker-compose build`
3. `docker-compose up`
4. You can check API responses with Postman if needed, you need form-data for the queries.

Queries:

POST

1. `localhost:8000/create` - Create an entry. Form fields are `name, price, year, label`.
2. `localhost:8000/update_year` - Update the year field for an entry with a certain ID. Form fields are `year,id`.
3. `localhost:8000/delete_one` - Delete one entry with a certain ID. Form field is `id`.

GET

1. `localhost:8000/read_all` - View all elements. Returns a list of list.