from django.db import models

class Customer(models.Model):
    ID = models.BigIntegerField(primary_key=True)
    lName = models.CharField(max_length=50)
    fName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    passW = models.CharField(max_length=20)
    isAdmin = models.BooleanField(default=False)

class Account(models.Model):
    accNumber = models.IntegerField(primary_key=True)
    accType = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    lastChangeDate = models.DateField()
    isActive = models.BooleanField(default=True)
    custID = models.ForeignKey(Customer, related_name='account', on_delete=models.CASCADE)
