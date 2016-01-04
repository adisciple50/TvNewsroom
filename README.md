# TvNewsroom
An Article Rest server with emergency broadcasts

## Prerequisits


Postgresql

Django

python 3.5

sphinx

## Dependacies


pip install git+https://github.com/nwcell/psycopg2-windows.git@win64-py34#egg=psycopg2

or

http://www.lfd.uci.edu/~gohlke/pythonlibs/

pip install djangorestframework

pip install django-admin-sortable

pip install django-hstore

pip install djangorestframework-hstore

pip install django-grappelli

pip install psycogreen

pip install -e git+https://github.com/abourget/gevent-socketio.git#egg=gevent_socketio-dev


## Setup

install the above dependacies using an admin command prompt / terminal

run this  sql on the database linked to the project - easy using pgadmin3

CREATE EXTENSION hstore;
