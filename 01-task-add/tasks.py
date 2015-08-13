import sys
print sys.version
print sys.executable
print sys.path

from time import sleep

from celery import Celery

app = Celery('tasks',broker='amqp://guest@rabbitmq-01.local//')

@app.task
def add(x,y):
    sleep(1)
    return x + y


