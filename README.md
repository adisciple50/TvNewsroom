# TvNewsroom
An Article Rest server with emergency broadcasts

## Prerequisits


Postgresql

Django

## Dependacies


pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py34#egg=psycopg2

or

http://www.lfd.uci.edu/~gohlke/pythonlibs/

pip install djangorestframework

pip install django-admin-sortable

pip install django-hstore

pip install djangorestframework-hstore


## Setup

run this  sql on the database linked to the project - easy using pgadmin3

CREATE EXTENSION hstore;
