from django.shortcuts import render

# Create your views here.

from celery_app.tasks import add


result = add.delay(2, 3)
print(result,"printing result")