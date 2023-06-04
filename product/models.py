from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)


class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
