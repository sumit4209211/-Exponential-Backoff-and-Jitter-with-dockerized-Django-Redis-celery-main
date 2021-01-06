# build a dockerized Django application with Redis, celery, and Postgres to handle asynchronous tasks

Initial configuration of Docker Django Redis Celery

This repository contains a sample store application demonstrating 
using Django with Paypal with Redis, celery, and Postgres to handle asynchronous tasks.

Retry the tasks. If the task fails, it's a good idea to try it again and again until it's executed successfully. You can do this in Celery with Celery Retry. One other interesting thing to look at is the Exponential Backoff algorithm. This could come in handy when thinking about limiting unnecessary load on the server from retried tasks.

Dockerized Django application with Redis, celery, and Postgres to handle asynchronous tasks



## Getting Started
This project works on Python 3+ and Django 2+.
Simply, run the following command:
```
docker-compose up --build
```
