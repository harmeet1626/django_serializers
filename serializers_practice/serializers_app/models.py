from django.db import models

class user_details(models.Model):
    user_id=models.IntegerField(primary_key = True)
    username= models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    class meta:
        db_table = "user_details"