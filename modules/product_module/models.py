from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    class Meta:
        app_label = 'product_module'

    def __str__(self):
        return self.name