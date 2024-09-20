from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Registartion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username


class ItemModel(models.Model):
    Item_name = models.CharField(max_length=30)
    Item_price = models.IntegerField(default=10)
    
    
    def __str__(self) -> str:
        return self.Item_name