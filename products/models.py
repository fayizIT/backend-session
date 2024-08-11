from django.db import models
from accounts.models import CustomUser,AccountInfo


class CampDetails(models.Model):
   
    camp_name = models.CharField(max_length=220)
    camp_status = models.BooleanField(default=False)
    camp_create_by = models.ForeignKey(CustomUser, related_name= 'camp_create_user', on_delete=models.CASCADE)
    camp_approved_by = models.ForeignKey(CustomUser, related_name= 'camp_approved_user', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pin_code = models.IntegerField()
    latitude =models.DecimalField(max_digits=30, decimal_places=20, default=None)
    longitude =models.DecimalField(max_digits=30, decimal_places=20, default=None)

    def __str__(self):
        return  f"{self.user} {self.latitude}{self.longitude}"


class Product(models.Model):

    class CategoryChoices(models.TextChoices):
        MEDICINE = 'medicine','Medicine'
        CLOTH = 'cloth', 'Cloth'
        FOOD = 'food', 'Food'
        STATIONARY = 'stationary', 'Stationary'

    class QuantityTypeChoices(models.TextChoices):
        KG = 'kg','Kg'
        GRAM = 'gram','Gram'
        Nos = 'nos','Nos'
        litre = 'litre','Litre'
        SMALL = 'small','Small'
        LARGE = 'large','Large'
    
    product_name = models.CharField(max_length=220)
    listed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    camp = models.ForeignKey(CampDetails,on_delete=models.CASCADE)
    listed_date = models.DateField(auto_now_add=True)
    required_date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    quantity_type = models.CharField(max_length=20, choices=QuantityTypeChoices.choices)
    category = models.CharField(max_length=20, choices=CategoryChoices.choices)
    urgent = models.BooleanField(default=True)


class Received_items(models.Model):

    received_item_name = models.CharField(max_length=220)
    sent_by = models.ForeignKey(CustomUser,related_name='sender', on_delete=models.CASCADE)
    receive_approved_by = models.ForeignKey(CustomUser,related_name='item_approved_admin', on_delete=models.CASCADE)
    received_camp_name = models.ForeignKey(CampDetails,related_name='items_received_camp', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    quantity_type = models.CharField(max_length=20)
    received_date = models.DateField()
    
    





