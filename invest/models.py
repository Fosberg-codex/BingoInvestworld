from enum import _auto_null
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    Phone = models.CharField(max_length=200)
    Referral_Code = models.CharField(max_length=200, null = True, default='', blank=True)
    
    VIP_Level = (('None','None'),
              ('VIP 1','VIP1'),
              ('VIP 2','VIP 2'),
              ('VIP 3','VIP 3'),
              ('VIP 4','VIP 4'),
              ('VIP 5','VIP 5'),
              ('VIP 6','VIP 6')
            )
    
    total_profit = models.CharField(max_length=200, default='$0', editable=False)
    amount_deposited = models.CharField(max_length=200, default='$0')
    amount_withdrawn = models.CharField(max_length=200, default='$0')
    number_of_transaction = models.CharField(max_length=200, default='0')
    personal_referral_code = models.CharField(max_length=200, null = True, default='(not available)')
    vip_level = models.CharField(max_length=300, null =True, choices= VIP_Level, default='None')
    
    def __str__(self):
        return f'Name: {self.username}-----------Personal_Refferal code: {self.personal_referral_code}-------VIP Level: {self.vip_level}'
    
    # def __str__(self):
    #     return self.username



# Create your models here.
# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     Phone = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     date_created = models.DateTimeField(auto_now_add=True,null=True)
    
#     def __str__(self):
#         return self.name


class Customers_Personal_Finance(models.Model):
    VIP_Level = (('None','None'),
              ('VIP 1','VIP1'),
              ('VIP 2','VIP 2'),
              ('VIP 3','VIP 3'),
              ('VIP 4','VIP 4'),
              ('VIP 5','VIP 5'),
              ('VIP 6','VIP 6')
            )
    
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL,related_name="Personal_finances")
    total_profit = models.CharField(max_length=200, default='$0', editable=False)
    amount_deposited = models.CharField(max_length=200, default='$0')
    amount_withdrawn = models.CharField(max_length=200, default='$0')
    number_of_transaction = models.CharField(max_length=200, default='0')
    referral_code = models.CharField(max_length=200, null = True, default='(not available)')
    vip_level = models.CharField(max_length=300, null =True, choices= VIP_Level, default='None')
    
    def __str__(self):
        return f'Name: {self.customer.username}----------- Refferal code{self.referral_code}-------VIP Level{self.vip_level}'
    
class Transaction_history(models.Model):
    Transaction_type = (('Deposit','Deposit'),
              ('Withdrawal','Withdrawal')
            )
    
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL, related_name="Transaction_history")
    Transaction_type = models.CharField(max_length=300, null =True, choices= Transaction_type)
    amount = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.customer.username