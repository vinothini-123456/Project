from django.db import models

# Create your models here.
class products(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField()
    product_desc=models.TextField()
    product_image=models.ImageField()

    def __str__(self):
        return self.product_name
