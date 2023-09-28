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

    # @property
    # def myName(self):
    #     a= address.objects.filter(PIN_code= 176061)
    #     # return a.values()
    #     return "Harmeet"



class address(models.Model):
    user_details = models.OneToOneField(user_details, on_delete=models.PROTECT,related_name= "user_details_child")
    city= models.CharField(max_length=255)
    State= models.CharField(max_length=255)
    PIN_code= models.IntegerField()
    class Meta:
        db_table = "address"

class course(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.CharField(max_length=200)
    updated_on = models.CharField(max_length=200)
    class Meta:
        db_table = "course"