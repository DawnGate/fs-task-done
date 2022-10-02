from celery import shared_task
from mail_manager.celery import app
from .views import getNewMailInCurrentMonth

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y

@app.task
def add30s(x,y):
    return x + y

@app.task
def newMailInCurrentMonth():
    print(getNewMailInCurrentMonth())