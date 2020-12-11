from django.db import models

# Create your models here.
class multiple_types(models.Model):
    regular=models.CharField(max_length=40)
    square=models.CharField(max_length=40)

class multiple_size(models.Model):
    small=models.CharField(max_length=40)
    medium=models.CharField(max_length=50)
    large=models.CharField(max_length=60)

class manny_toppings(models.Model):
    onion=models.CharField(max_length=40)
    tomato=models.CharField(max_length=50)
    corn=models.CharField(max_length=60)
    capsicum=models.CharField(max_length=60)
    cheese=models.CharField(max_length=60)
    jalapeno=models.CharField(max_length=60)







