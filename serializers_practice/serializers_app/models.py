from django.db import models

class user_details(models.Model):
    username= models.CharField(max_length=255)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    class Meta:
        db_table = "user_details"



class address(models.Model):
    user_details = models.OneToOneField(user_details, on_delete=models.PROTECT,related_name= "user_details_child")
    city= models.CharField(max_length=255)
    State= models.CharField(max_length=255)
    PIN_code= models.IntegerField()
    class Meta:
        db_table = "address"
