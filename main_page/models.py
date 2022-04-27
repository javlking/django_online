from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class ProductName(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=350)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, default=10000)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product_name = models.CharField(max_length=100)
    product_count = models.IntegerField()
    user_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id