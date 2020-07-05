from django.db import models


class Customer(models.Model):
    """Customer model: all information about customer"""
    username = models.CharField(max_length=64, unique=True)
    spent_money = models.IntegerField()


class Deal(models.Model):
    """Deal model: all information about deal"""
    gem_name = models.CharField(max_length=64)
    quantity = models.IntegerField()
    date_of_deal = models.DateTimeField()
    total_price = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="deals")


class FileCSV(models.Model):
    """File model"""
    file = models.FileField(upload_to='files/', blank=False, null=False)