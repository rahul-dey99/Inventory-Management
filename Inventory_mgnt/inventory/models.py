from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    prodect_description = models.TextField(max_length=150)
    num_in_inventory = models.CharField(max_length=150)
    product_image = models.ImageField()