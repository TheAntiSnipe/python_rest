### This repository contains some basic design pattern work done by me.

Note that these patterns are quite redundant for various reasons considering the scale of the project, and are intended purely for practice.

The application is a RESTful CRUD API served through a container that exposes port 8000. It's built with the help of Flask, with the psycopg2 library being used for DB handling.

The structure is a PostgreSQL Docker container hooked up to a Python image with Flask and Psycopg2 packages installed.

Uses the facade pattern for QueryHandler, along with the subsystem pattern. For the database connection handler, a Borg Singleton is showcased.