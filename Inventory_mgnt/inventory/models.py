from django.db import models

class Inventory(models.Model):
    inventory_name = models.CharField(max_length=100)
    inventory_type = models.CharField(max_length=100)
    inventory_description = models.TextField()

    def __str__(self):
        return f'{self.inventory_name}'

class Product(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True) 
    product_name = models.CharField(max_length=150)
    product_description = models.TextField(default=None)
    num_in_inventory = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product_img/', null=True)
