from django.db import models


# product model

class Product(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField()
    price = models.FloatField(max_length=10)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
