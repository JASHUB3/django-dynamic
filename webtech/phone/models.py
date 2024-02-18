from django.db import models

# Create your models here.

class Item(models.Model):
    item =models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.item


class Product(models.Model):
    name =models.CharField(max_length=100)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    release_date = models.DateField()
    product_sp = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name

    
