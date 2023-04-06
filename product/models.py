from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(validators=[MinValueValidator(0)])  #PositiveIntegerField()

    def __str__(self):
        return f'{self.name}: {self.price}원'
