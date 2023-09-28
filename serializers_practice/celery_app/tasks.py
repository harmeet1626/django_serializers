from celery import shared_task
  
  
@shared_task
def add(x, y):
    print("Printed ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return x + y

add(1,2)

# use to run celery :- celery -A celery_app worker -l info 
